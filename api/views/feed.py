from feed.models import Conversation, Reply
from api.serializers.feed import CommentSerializer, ReplySerializer, ValidateCommentSerializer, ValidateReplySerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

def validate_serializer(serializer, request):
    instance = serializer(data=request.data)
    instance.is_valid(raise_exception=True) 
    return instance


@api_view(['get'])
def get_conversations(request, **kwargs):
    queryset = Conversation.objects.all()
    serializer = CommentSerializer(instance=queryset, many=True)
    return Response(data=serializer.data)


@api_view(['get'])
def get_replies(request, **kwargs):
    queryset = Reply.objects.all()
    serializer = ReplySerializer(instance=queryset, many=True)
    return Response(data=serializer.data)


@api_view(['post'])
def create_conversation(request, **kwargs):
    serializer = validate_serializer(ValidateCommentSerializer, request)
    serializer.save(request)
    return Response(data=serializer.data)


@api_view(['post'])
def create_reply(request, **kwargs):
    serializer = validate_serializer(ValidateReplySerializer, request)
    serializer.save(request)
    return Response(data=serializer.data)

