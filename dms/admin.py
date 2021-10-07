from django.contrib import admin

from dms.models import DirectMessage


@admin.register(DirectMessage)
class DirectMessagesAdmin(admin.ModelAdmin):
    list_display = ['message_sender', 'message_receiver', 'created_on']
