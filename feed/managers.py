from django.db.models import QuerySet
from django.db.models.aggregates import Count
from django.db.models.expressions import Q, Case, When
from django.db.models import BooleanField


class ConversationsManager(QuerySet):
    @staticmethod
    def annotate_comment(queryset, user=None):
        annotated_queryset = queryset.annotate(likes=Count('like__id'), replies=Count('reply__id'))
        if user is not None:
            # When the user is logged in, return the current
            # post was liked or not for the front end
            logic = When(Q(like__user__id=user), then=True)
            cases = Case(logic, default=False, output_field=BooleanField())
            return annotated_queryset.annotate(liked=cases)
        return annotated_queryset

    def search(self, q, only_users=False):
        # Search for a specific item in comments
        # and replies from the database
        
        # TODO: To optimize search on the database,
        # when the value starts with an @,
        # we'll only directly search for users
        # and their conversations or replies
        
        
        logic = (
            Q(text__icontains=q) |
            Q(user__username__icontains=q) |
            Q(reply__text__icontains=q)
        )
        return self.prefetch_related('reply_set').filter(logic)

    def timeline(self, follows_ids):
        # For the timeline, only return the conversations
        # that were created by the users that the current
        # user is following
        queryset = self.filter(user__id__in=follows_ids, scheduled=False)
        return self.annotate_comment(queryset).order_by('-created_on')

    def annoted_conversations(self, username, follows_ids=None, queryset=None):
        # user_in_likes = When(like__user__username=username, then=True)
        # cases = Case(user_in_likes, default=False, output_field=BooleanField())
        # if queryset:
        #     return queryset.annotate(has_liked=cases)
        # return self.timeline(follows_ids).annotate(has_liked=cases)
        return self.timeline(follows_ids)


class RepliesManager(QuerySet):
    @staticmethod
    def annotate_reply(queryset, user=None):
        annotated_queryset = queryset.annotate(likes=Count('like__id'))
        if user is not None:
            # When the user is logged in, return the current
            # post was liked or not for the front end
            logic = When(Q(like__user__id=user), then=True)
            cases = Case(logic, default=False, output_field=BooleanField())
            return annotated_queryset.annotate(liked=cases)
        return annotated_queryset
    
    def replies_for_comment(self, pk, user=None):
        # Get all the replies for a comment
        if hasattr(user, 'id'):
            user = getattr(user, 'id')

        replies = self.filter(conversation__id=pk)
        return self.annotate_reply(replies, user=user)     
