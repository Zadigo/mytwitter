from api.serializers.mixins import SerializerMixin
from api.serializers.users import UserSerializer
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import fields
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.serializers import Serializer
from rest_framework.viewsets import GenericViewSet

from feed.models import Conversation, Reply

USER_MODEL = get_user_model()

class AbstractMessageSerializer(Serializer):
    id = fields.IntegerField(read_only=True)
    user = UserSerializer(read_only=True)
    text = fields.CharField()
    liked = fields.BooleanField(default=False, read_only=True)
    created_on = fields.DateTimeField(read_only=True)


class CommentSerializer(AbstractMessageSerializer):
    """Conversation serializer"""

    likes = fields.IntegerField(read_only=True)


class ReplySerializer(SerializerMixin, AbstractMessageSerializer):
    conversation = CommentSerializer(read_only=True)
    likes = fields.IntegerField(read_only=True)

    def create(self, request, validated_data):
        conversation = get_object_or_404(Conversation, id=validated_data['conversation_id'])
        reply = conversation.reply_set.create(
            user=request.user,
            text=validated_data['text']
        )
        return reply


class ValidateCommentSerializer(SerializerMixin, Serializer):
    text = fields.CharField(max_length=255)

    def create(self, request, validated_data):
        return Conversation.objects.create(
            user=request.user,
            text=validated_data['text']
        )


class ValidateReplySerializer(SerializerMixin, Serializer):
    text = fields.CharField(max_length=255)

    def create(self, request, validated_data):
        conversation = get_object_or_404(
            Conversation,
            id=validated_data['conversation_id']
        )
        reply = Reply.objects.create(
            conversation=conversation,
            user=request.user,
            text=validated_data['text']
        )
        return reply
