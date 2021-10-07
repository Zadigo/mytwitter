from django.contrib.auth import get_user_model
from rest_framework.serializers import Serializer
from api.serializers.users import UserSerializer, ValidateFollowingSerializer
from rest_framework.decorators import api_view
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response

from dms.models import USER_MODEL


USER_MODEL = get_user_model()

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
    queryset = USER_MODEL.objects.all()
    serializer_class = UserSerializer

