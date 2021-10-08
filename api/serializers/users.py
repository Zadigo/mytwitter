from accounts.models import MyUser
from rest_framework import fields
from rest_framework.serializers import Serializer


class UserSerializer(Serializer):
    id = fields.IntegerField(read_only=True)
    username = fields.CharField()
    get_full_name = fields.CharField()


class ValidateFollowingSerializer(Serializer):
    user_to_follow = fields.IntegerField()
    user_following = fields.IntegerField()

    def _follow_user(self, request):
        pass

    def _unfollow_user(self, request):
        pass

    def create(self, validated_data):
        pass

    def save(self, request, method='follow', **kwargs):
        return super().save(**kwargs)
