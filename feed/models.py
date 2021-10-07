from django.contrib.auth import get_user_model
from django.db import models
from django.views.decorators.cache import cache_control

from feed import managers

MYUSER = get_user_model()

class Conversation(models.Model):
    body = models.CharField(max_length=255)
    created_by = models.ForeignKey(MYUSER, on_delete=models.DO_NOTHING)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        indexes = [
            models.Index(fields=['created_by'])
        ]

    objects = models.Manager()
    conversations_manager = managers.ConversationsManager.as_manager()

    def __str__(self):
        return self.created_by.username


class Reply(models.Model):
    user = models.ForeignKey(MYUSER, on_delete=models.CASCADE)
    conversation = models.ForeignKey(Conversation, on_delete=models.DO_NOTHING, blank=True, null=True)
    text = models.CharField(max_length=255, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Replies'
        ordering = ['-created_on', '-pk']

    def __str__(self):
        return self.conversation.created_by
