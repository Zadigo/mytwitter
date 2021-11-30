from django.contrib import admin
from accounts.admin import custom_site
from feed.models import Conversation, Hashtag, Reply

class ConversationAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_on']
    date_hierarchy = 'created_on'


class ReplyAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_on']
    date_hierarchy = 'created_on'
    
    
class HashtagAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_on']
    date_hiearchy = 'crated_on'
    search_fields = ['name']


custom_site.register(Conversation, ConversationAdmin)
custom_site.register(Reply, ReplyAdmin)
custom_site.register(Hashtag, HashtagAdmin)
