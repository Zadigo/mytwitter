from django.contrib import admin
from dms import models

@admin.register(models.DirectMessage)
class DirectMessagesAdmin(admin.ModelAdmin):
    list_display = ['message_sender', 'message_receiver', 'created_on']
