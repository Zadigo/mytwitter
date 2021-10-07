from api.serializers.feed import CommentSerializer, ReplySerializer
from api.serializers.users import UserSerializer
from rest_framework import fields
from rest_framework.serializers import Serializer

from likes.models import Like


class LikeSerializer(Serializer):
    user = UserSerializer()
    conversation = CommentSerializer()
