from likes.models import Like
from rest_framework.serializers import Serializer
from rest_framework import fields
from api.serializers.users import UserSerializer
from api.serializers.feed import CommentSerializer, ReplySerializer

class LikeSerializer(Serializer):
    user = UserSerializer()
    conversation = CommentSerializer()
