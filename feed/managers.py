from django.db.models import QuerySet
from django.db.models.expressions import Q, Case, When
from django.db.models import BooleanField


class ConversationsManager(QuerySet):
    def search(self, q):
        logic = (
            Q(body__icontains=q) |
            Q(created_by__username__icontains=q)
        )
        return self.filter(logic)

    def timeline(self, follows_ids):
        return self.filter(created_by__id__in=follows_ids)

    def annoted_conversations(self, username, follows_ids=None, queryset=None):
        # user_in_likes = When(like__user__username=username, then=True)
        # cases = Case(user_in_likes, default=False, output_field=BooleanField())
        # if queryset:
        #     return queryset.annotate(has_liked=cases)
        # return self.timeline(follows_ids).annotate(has_liked=cases)
        return self.timeline(follows_ids)
        
