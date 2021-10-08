from api.serializers.authentication import LoginSerializer
from django.contrib.auth import logout
from django.db.models import query
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['post'])
def login_view(request, **kwargs):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    instance, state = serializer.save(request)
    return Response(data={'token': instance.key}, status=status.HTTP_200_OK)


@api_view(['post'])
def logout_view(request, **kwargs):
    authorization_token = request.META.get('authorization')
    queryset = Token.objects.filter(token=authorization_token)
    if queryset.exists():
        try:
            token = queryset.get()
        except:
            return Response(data={'error': 'Failed'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            token.delete()
            logout(request)
    return Response(data={'message': 'Success'}, status=status.HTTP_200_OK)
