from django.db.models import QuerySet
from django.db.models.aggregates import Count
from django.db.models.expressions import Q, Case, When
from django.db.models import BooleanField


class ConversationsManager(QuerySet):
    @staticmethod
    def annotate_comment(queryset, user=None):
        annotated_queryset = queryset.annotate(likes=Count('like__id'))
        if user is not None:
            # When the user is logged in, return the current
            # post was liked or not for the front end
            logic = When(Q(like__user__id=user), then=True)
            cases = Case(logic, default=False, output_field=BooleanField())
            return annotated_queryset.annotate(liked=cases)
        return annotated_queryset

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

    def replies_for_comment(self, pk, user=None):
        """Get all the replies for a comment and if the
        user is authenticated, indicate if specific posts
        where liked by him"""
        if hasattr(user, 'id'):
            user = getattr(user, 'id')

        comment = self.get(id=pk)
        replies = comment.reply_set.all()
        return self.annotate_comment(replies, user=user)     
