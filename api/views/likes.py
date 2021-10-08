from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from feed.models import Conversation, Reply
from likes.models import Like

@api_view(['post'])
def create_like(request, method, pk, **kwargs):
    methods = ['replies', 'conversations']
    response_attrs = {
        'data': {
            'message': None
        },
        'status': status.HTTP_200_OK
    }

    if method not in methods:
        response_attrs['data']['message'] = 'Could not vote'
        response_attrs['status'] = status.HTTP_500_INTERNAL_SERVER_ERROR

    def toggle_vote(obj):
        # When the post is already liked,
        # delete the like, other, just
        # create one
        likes = obj.like_set.all()
        if likes.exists():
            likes.delete()
        else:
            obj.like_set.create(user=request.user)

    if method == 'replies':
        reply = get_object_or_404(Reply, id=pk)
        toggle_vote(reply)

    if method == 'conversations':
        conversation = get_object_or_404(Conversation, id=pk)
        toggle_vote(conversation)

    return Response(**response_attrs)
