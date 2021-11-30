from django.shortcuts import get_object_or_404
from accounts.models import MyUserProfile
from api.serializers.feed import (CommentSerializer, ReplySerializer,
                                  ValidateCommentSerializer,
                                  ValidateReplySerializer)
from django.db.models import Count
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from feed.models import Conversation, Reply


def validate_serializer(serializer, request, **kwargs):
    instance = serializer(data=request.data, **kwargs)
    instance.is_valid(raise_exception=True) 
    return instance


@api_view(['get'])
def get_conversations(request, **kwargs):
    if not request.user.is_authenticated:
        pass
    user_profile = get_object_or_404(MyUserProfile, id=2)
    following = user_profile.follows.values_list('id', flat=True)
    timeline_comments = Conversation.objects.timeline(following)
    serializer = CommentSerializer(instance=timeline_comments, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['get'])
def get_replies(request, pk, **kwargs):
    annotated_queryset = Reply.objects.replies_for_comment(pk)
    serializer = ReplySerializer(instance=annotated_queryset, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['post'])
def create_conversation(request, **kwargs):
    serializer = validate_serializer(ValidateCommentSerializer, request)
    comment = serializer.save(request)
    serializer = CommentSerializer(instance=comment)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['post'])
def create_reply(request, pk, **kwargs):
    serializer = validate_serializer(ReplySerializer, request)
    reply = serializer.save(request, conversation_id=pk)
    replies = Conversation.objects.replies_for_comment(pk, user=request.user.id)
    serializer = ReplySerializer(instance=replies, many=True)
    return Response(data=serializer.data)
