from accounts import widgets as custom_widgets
from accounts.models import MyUser, MyUserProfile
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.tokens import default_token_generator
from django.core.exceptions import ValidationError
from django.forms import fields, widgets
from django.contrib.auth.forms import UsernameField
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _

USER_MODEL = get_user_model()

class AuthenticationForm(forms.Form):
    """Replaces the admin authentication form with one that 
    allows login with email"""

    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
    )

    error_messages = {
        'invalid_login': _(
            "Please enter a correct %(username)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        'inactive': _("This account is inactive."),
    }

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        super().__init__(*args, **kwargs)
        self.username_field = USER_MODEL._meta.get_field(USER_MODEL.USERNAME_FIELD)

    def clean(self):
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if email is not None and password:
            self.user_cache = authenticate(self.request, email=email, password=password)
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    def confirm_login_allowed(self, user):
        """
        Controls whether the given User may log in. This is a policy setting,
        independent of end-user authentication. This default behavior is to
        allow login by active users, and reject login by inactive users.

        If the given user cannot log in, this method should raise a
        ``ValidationError``.

        If the given user may log in, this method should return None.
        """
        if not user.is_active:
            raise ValidationError(
                self.error_messages['inactive'],
                code='inactive',
            )

    def get_user(self):
        return self.user_cache

    def get_invalid_login_error(self):
        return ValidationError(
            self.error_messages['invalid_login'],
            code='invalid_login',
            params={'username': self.username_field.verbose_name},
        )

class CustomAdminAuthenticationForm(AuthenticationForm):
    """A custom form to allow authentication with email field"""

    error_messages = {
        **AuthenticationForm.error_messages,
        'invalid_login': _(
            "Please enter the correct %(username)s and password for a staff "
            "account. Note that both fields may be case-sensitive."
        ),
    }
    required_css_class = 'required'

    def confirm_login_allowed(self, user):
        super().confirm_login_allowed(user)
        if not user.is_staff:
            raise ValidationError(
                self.error_messages['invalid_login'],
                code='invalid_login',
                params={'username': self.username_field.verbose_name}
            )


class MyUserCreationForm(forms.ModelForm):
    password1 = fields.CharField(label=_('Password'), widget=widgets.PasswordInput)
    password2 = fields.CharField(label=_('Password confirmation'), widget=widgets.PasswordInput)

    class Meta:
        model = MyUser
        fields = ['email', 'is_admin', 'is_staff']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_("Passwords don't match"))

        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()

        return user
        

class MyUserChangeForm(forms.ModelForm):
    password = auth_forms.ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ['email', 'password']

    def clean_password(self):
        return self.initial['password']
