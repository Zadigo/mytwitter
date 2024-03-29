import stripe
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import functional, timezone
from django.utils.translation import gettext_lazy as _
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToCover

from accounts.managers import MyUserManager
from accounts.utils import upload_to


class MyUser(AbstractBaseUser):
    """Base user model for those user accounts"""
    email       = models.EmailField(max_length=255, unique=True)
    firstname      = models.CharField(max_length=100, null=True, blank=True)
    lastname         = models.CharField(max_length=100, null=True, blank=True)
    username         = models.CharField(max_length=50, null=True, blank=True, unique=True)
    
    is_active        = models.BooleanField(default=True)
    is_admin            = models.BooleanField(default=False)
    is_staff            = models.BooleanField(default=False)
    
    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def get_full_name(self):
        return f'{self.firstname} {self.lastname}' 

    @property
    def get_short_name(self):
        return self.firstname

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    # def save(self, *args, **kwargs):
    #     if self._state.adding:
    #         super().save(*args, **kwargs)
    #         profile = MyUserProfile.objects.create(myuser=self)
    #         try:
    #             details = stripe.Customer.create(email=self.email, name=self.get_full_name)
    #         except stripe.error.StripeError as e:
    #             print(e.args)
    #         except Exception as e:
    #             print(e.args)
    #         else:
    #             profile.customer_id = details['id']
    #             profile.save()


class MyUserProfile(models.Model):
    """User profile model used to complete the base user model"""
    myuser = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    customer_id = models.CharField(max_length=100, blank=True, null=True, help_text='Stripe customer ID')
    birthdate = models.DateField(default=timezone.now, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)
    city  = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.IntegerField(blank=True, null=True)

    follows   = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)
    avatar   = ProcessedImageField(
        processors=[ResizeToCover(100, 100)],
        format='JPEG',
        options={'quality': 80},
        upload_to=upload_to,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.myuser.email

    @property
    def get_full_address(self):
        return f'{self.address}, {self.city}, {self.zip_code}'

    @functional.cached_property
    def get_followers(self):
        return self.follows.all().count()


class SubscribedUser(models.Model):
    """People who subscribed to the website"""
    email       = models.EmailField(blank=True, null=True)
    created_on  = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email


@receiver(post_save, sender=MyUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        MyUserProfile.objects.create(myuser=instance)
