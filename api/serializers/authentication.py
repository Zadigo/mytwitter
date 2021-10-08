from rest_framework import fields

from accounts.models import MyUser
from rest_framework.serializers import Serializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, get_user_model, login
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

USER_MODEL = get_user_model()

class LoginSerializer(Serializer):
    username = fields.CharField(max_length=100, required=True)
    password = fields.CharField(max_length=100, required=True)

    def save(self, request, **kwargs):
        validated_data = {**self.validated_data, **kwargs}

        if self.instance is not None:
            self.instance = self.update(self.instance, validated_data)
        else:
            self.instance = self.create(request, validated_data)

        if self.instance is None:
            raise ValueError('Instance was not created')

        return self.instance

    def create(self, request, validated_data):
        # Since we are using email authentication,
        # we have to retrieve the email 
        # to authenticate the user
        user = get_object_or_404(USER_MODEL, username=validated_data['username'])

        attrs = {
            'email': user.email,
            'password': validated_data['password']
        }
        user = authenticate(request, **attrs)
        if user:    
            return Token.objects.get_or_create(user=user)
        return False, None
