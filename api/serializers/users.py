from accounts.models import MyUser
from rest_framework.serializers import Serializer
from rest_framework import fields


class UserSerializer(Serializer):
    username = fields.CharField()
