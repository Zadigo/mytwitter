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
    queryset = Conversation.objects.all()
    annotated_comments = queryset.annotate(
        likes=Count('like__id'),
        replies=Count('reply__id')
    )
    serializer = CommentSerializer(instance=annotated_comments, many=True)
    return Response(data=serializer.data)


@api_view(['get'])
def get_replies(request, pk, **kwargs):
    # queryset = Reply.objects.filter(conversation__id=pk)
    # annotated_queryset = queryset.annotate(likes=Count('like__id'))
    annotated_queryset = Conversation.objects.replies_for_comment(pk, user=request.user)
    serializer = ReplySerializer(instance=annotated_queryset, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['post'])
def create_conversation(request, **kwargs):
    serializer = validate_serializer(ValidateCommentSerializer, request)
    comment = serializer.save(request)
    queryset = Conversation.objects.all()
    serializer = CommentSerializer(instance=queryset, many=True)
    return Response(data=serializer.data)


@api_view(['post'])
def create_reply(request, pk, **kwargs):
    serializer = validate_serializer(ReplySerializer, request)
    reply = serializer.save(request, conversation_id=pk)
    replies = Conversation.objects.replies_for_comment(pk, user=request.user.id)
    serializer = ReplySerializer(instance=replies, many=True)
    return Response(data=serializer.data)
