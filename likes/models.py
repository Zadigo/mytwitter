from django.contrib.auth import get_user_model
from django.db import models
from feed.models import Conversation, Reply

USER_MODEL = get_user_model()

class Like(models.Model):
    user = models.ForeignKey(
        USER_MODEL,
        on_delete=models.CASCADE
    )
    reply = models.ForeignKey(
        Reply,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )
    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )

    def __str__(self):
        if self.reply is not None:
            return self.reply.user.username
        return self.conversation.user.username
