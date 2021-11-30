from api.serializers.direct_messages import DirectMessageSerializer
from dms.models import DirectMessage
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from rest_framework.decorators import api_view

@api_view(['get'])
def get_direct_messages(request, user_id, **kwargs):
    logic = (
        Q(message_sender__id=user_id) |
        Q(message_receiver__id=user_id)
    )
    queryset = DirectMessage.objects.filter(logic)
    serializer = DirectMessageSerializer(instance=queryset, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)
