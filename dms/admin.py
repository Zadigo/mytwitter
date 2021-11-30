from django.contrib import admin
from accounts.admin import custom_site

from dms.models import DirectMessage


class DirectMessagesAdmin(admin.ModelAdmin):
    list_display = ['message_sender', 'message_receiver', 'created_on']
    date_hiearchy = 'created_on'


custom_site.register(DirectMessage, DirectMessagesAdmin)
