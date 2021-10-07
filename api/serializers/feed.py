from api.serializers.users import UserSerializer
from dms.models import Feed
from rest_framework import fields
from rest_framework.serializers import Serializer


class CommentSerializer(Serializer):
    body = fields.CharField()
    created_by = fields.DateFiedl()
    created_on = fields.DateField()


class ReplySerializer(Serializer):
    reply = CommentSerializer()
    user = UserSerializer()
    text = fields.CharField()
    created_on = fields.DateField()


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
