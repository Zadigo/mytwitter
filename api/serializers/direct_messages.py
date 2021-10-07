from api.serializers.users import UserSerializer
from dms.models import DirectMessage
from rest_framework import fields
from rest_framework.serializers import Serializer

class DirectMessageSerializer(Serializer):
    message_sender = UserSerializer()
    message_receiver = UserSerializer()
    text = fields.TextField()
    created_on = fields.DateField()
