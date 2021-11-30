from django.db.models import QuerySet
from django.db.models.expressions import Q

class DirectMessageManager(QuerySet):
    def my_messages(self, user, queryset=None):
        logic = (
            Q(message_sender=user.id) | 
            Q(message_receiver=user.id)
        )
        if queryset is not None:
            return queryset.filter(logic)
        return self.filter(logic)

    def messages_with_specific_user(self, user, receiver, queryset=None):
        messages = self.my_messages(user, queryset=queryset)
        logic = (
            Q(message_receiver__username=receiver.username) | 
            Q(message_sender__username=receiver.username)
        )
        return messages.filter(logic)
