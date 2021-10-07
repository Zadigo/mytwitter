from django.db import models
from django.contrib.auth import get_user_model

USER_MODEL = get_user_model()

class Like(models.Model):
    user = models.ForeignKey(USER_MODEL, on_delete=models.CASCADE)
    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )
    # reply = models.ForeignKey(Reply, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return str(self.conversation.created_by)
