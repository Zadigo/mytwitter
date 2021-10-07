from api.serializers.users import UserSerializer
from feed.models import Conversation
from rest_framework import fields
from rest_framework.serializers import Serializer


class AbstractMessageSerializer(Serializer):
    user = UserSerializer()
    text = fields.CharField()
    created_by = fields.DateField()
    created_on = fields.DateField()


class CommentSerializer(AbstractMessageSerializer):
    """Conversation serializer"""


class ReplySerializer(AbstractMessageSerializer):
    reply = CommentSerializer()
    text = fields.CharField()


class ValidateCommentSerializer(Serializer):
    user = fields.IntegerField()
    body = fields.CharField()

    def create(self, request, **kwargs):
        pass


class ValidateReplySerializer(Serializer):
    user = fields.IntegerField()
    body = fields.CharField()

    def create(self, request, **kwargs):
        pass
