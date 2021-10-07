from django.contrib import admin
from accounts.admin import custom_site
from feed.models import Conversation, Reply

class ConversationAdmin(admin.ModelAdmin):
    list_display = ['user']
    date_hierarchy = 'created_on'


class ReplyAdmin(admin.ModelAdmin):
    list_display = ['user']
    date_hierarchy = 'created_on'


custom_site.register(Conversation, ConversationAdmin)
custom_site.register(Reply, ReplyAdmin)
