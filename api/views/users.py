from api.serializers.users import UserSerializer, ValidateFollowingSerializer
from django.contrib.auth import get_user_model
from dms.models import USER_MODEL
from rest_framework.decorators import api_view
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.viewsets import GenericViewSet

USER_MODEL = get_user_model()

class PaginateMessages(LimitOffsetPagination):
    default_limit = 100
    max_limit = 100


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


class UsersView(GenericViewSet, RetrieveModelMixin):
    http_method_names = ['get']
    queryset = USER_MODEL.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
