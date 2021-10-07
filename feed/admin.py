from django.contrib import admin
from feed.models import Conversation, Reply

@admin.register(Conversation)
class TimeLineAdmin(admin.ModelAdmin):
    list_display = ['user']
    date_hierarchy = 'created_on'
