from rest_framework.serializers import Serializer
from api.serializers.users import UserSerializer, ValidateFollowingSerializer
from rest_framework.decorators import api_view
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response


@api_view(['post'])
def follow_user(request, **kwargs):
    serializer = ValidateFollowingSerializer(data=request.data)
    serializer.save(request,)
    return Response(data=serializer.data)


@api_view(['post'])
def unfollow_user(request, **kwargs):
    serializer = ValidateFollowingSerializer(data=request.data)
    serializer.save(request, method='unfollow')
    return Response(data=serializer.data)


class UserTimelineView(GenericViewSet, RetrieveModelMixin):
    http_method_names = ['get']
    serializer_class = UserSerializer

