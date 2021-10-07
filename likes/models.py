from django.db import models


class Like(models.Model):
    user = models.ForeignKey(MYUSER, on_delete=models.CASCADE)
    conversation = models.ForeignKey(
        Conversation, on_delete=models.DO_NOTHING, blank=True, null=True)
    # reply = models.ForeignKey(Reply, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return str(self.conversation.created_by)
