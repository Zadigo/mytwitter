from django.contrib.auth import get_user_model
from django.db import models
from feed.choices import VisibilityChoices
from django.utils import timezone

from feed.managers import ConversationsManager, RepliesManager
from feed.validators import validate_scheduling_date

USER_MODEL = get_user_model()


class Hashtag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_on', 'pk']
    
    def __str__(self):
        return self.name


class AbstractMessage(models.Model):
    user = models.ForeignKey(
        USER_MODEL,
        on_delete=models.CASCADE
    )
    text = models.CharField(max_length=255, blank=True, null=True)
    visibility = models.CharField(
        max_length=100,
        choices=VisibilityChoices.choices,
        default=VisibilityChoices.PUBLIC
    )
    hashtags = models.ManyToManyField(
      Hashtag,
      blank=True
    )
    # mentions = models.ManyToManyField(
    #     USER_MODEL,
    #     null=True
    # )
    # limited_to_users = models.ManyToManyField(
    #     USER_MODEL,
    #     related_name='only_users_can_reply',
    #     related_query_name='for_users',
    #     null=True
    # )
    schedule = models.DateTimeField(
        default=timezone.now,
        blank=True,
        null=True,
        validators=[validate_scheduling_date]
    )
    scheduled = models.BooleanField(default=False)
    
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ['-created_on', '-pk']
        indexes = [
            models.Index(fields=['user'])
        ]

    def __str__(self):
        return self.user.username


class Conversation(AbstractMessage):
    objects = ConversationsManager.as_manager()


class Reply(AbstractMessage):
    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )
    
    objects = RepliesManager.as_manager()

    class Meta(AbstractMessage.Meta):
        verbose_name_plural = 'Replies'
