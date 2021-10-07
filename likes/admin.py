from django.contrib import admin
from accounts.admin import custom_site
from likes.models import Like


class LikeAdmin(admin.ModelAdmin):
    list_display = ['conversation']

custom_site.register(Like, LikeAdmin)
