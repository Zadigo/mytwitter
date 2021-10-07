from rest_framework.response import Response
from api.serializers.likes import LikeSerializer
from rest_framework.decorators import api_view
from likes.models import Like

@api_view(['post'])
def create_like(request, method, **kwargs):
    queryset = Like.objects.all()
    serializer = LikeSerializer(instance=queryset, many=True)
    return Response(data=serializer.data)
