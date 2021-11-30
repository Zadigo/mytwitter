from api.serializers.users import UserSerializer
from dms.models import DirectMessage
from rest_framework import fields
from rest_framework.serializers import Serializer


class DirectMessageSerializer(Serializer):
    id = fields.IntegerField(read_only=True)
    message_receiver = UserSerializer()
    message_sender = UserSerializer()
    text = fields.CharField()
    created_on = fields.DateTimeField()
