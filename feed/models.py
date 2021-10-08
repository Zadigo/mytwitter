from django.contrib.auth import get_user_model
from django.db import models

from feed.managers import ConversationsManager

USER_MODEL = get_user_model()

class AbstractMessage(models.Model):
    user = models.ForeignKey(
        USER_MODEL,
        on_delete=models.CASCADE
    )
    text = models.CharField(max_length=255, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ['-created_on', '-pk']
        indexes = [
            models.Index(fields=['user'])
        ]

    def __str__(self):
        return self.user.username


class Conversation(AbstractMessage):
    objects = ConversationsManager.as_manager()



class Reply(AbstractMessage):
    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )

    class Meta(AbstractMessage.Meta):
        verbose_name_plural = 'Replies'
