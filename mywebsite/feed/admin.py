from django.contrib import admin
from feed import models

@admin.register(models.Conversation)
class TimeLineAdmin(admin.ModelAdmin):
    list_display = ['created_by']
    date_hierarchy = 'created_on'
