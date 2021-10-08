from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth import admin as auth_admin
from django.contrib.auth.models import Group
from rest_framework.authtoken.models import Token
from django.utils.translation import gettext_lazy as _

from accounts import forms, models
from accounts.forms.admin import CustomAdminAuthenticationForm, MyUserChangeForm, MyUserCreationForm


class CustomAdminSite(AdminSite):
    login_form = CustomAdminAuthenticationForm

custom_site = CustomAdminSite()


class MyUserAdmin(auth_admin.UserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    model = models.MyUser

    list_display = ['email', 'firstname', 'lastname', 'is_active', 'is_admin']
    list_filter = ()
    filter_horizontal = ()
    ordering = ['email']
    search_fields = ['firstname', 'lastname', 'email']
    fieldsets = [
        ['Details', {'fields': ['firstname', 'lastname', 'username']}],
        ['Credentials', {'fields': ['email', 'password']}],
        ['Permissions', {'fields': ['is_admin', 'is_staff', 'is_active']}]
    ]
    add_fieldsets = [
        [None, {
                'classes': ['wide'],
                'fields': ['email', 'username', 'password1', 'password2', 'is_admin', 'is_staff', 'is_active']
            }
        ],
    ]
    ordering = ['email']


class MyUserProfileAdmin(admin.ModelAdmin):
    actions      = ('activate_account', 'deactivate_account',)
    list_display = ('myuser', 'telephone',)
    search_fields = ['myuser__firstname', 'myuser__lastname', 'myuser__email']

    def activate_account(self, request, queryset):
        queryset.update(actif=True)

    def deactivate_account(self, request, queryset):
        queryset.update(actif=False)


class SubscribedUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'created_on']
    date_hierarchy = 'created_on'
    list_filter = ['created_on']


# admin.site.unregister(Group)
custom_site.register(models.MyUser, MyUserAdmin)
custom_site.register(models.MyUserProfile, MyUserProfileAdmin)
custom_site.register(Token)
# custom_admin.register(models.SubscribedUser, models.SubscribedUser)
