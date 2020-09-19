from django.db import models
from django.contrib.auth import get_user_model
from dms import managers

MYUSER = get_user_model()

class DirectMessage(models.Model):
    message_sender      = models.ForeignKey(MYUSER, on_delete=models.CASCADE, related_name='sender')
    message_receiver    = models.ForeignKey(MYUSER, on_delete=models.CASCADE, related_name='receiver')
    text            = models.CharField(max_length=200)
    created_on      = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    objects = models.Manager()
    messages_manager = managers.DirectMessageManager.as_manager()

    def __str__(self):
        return self.message_sender.username
