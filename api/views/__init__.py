from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404

def authenticate_token(request):
    token = request.META.get('authorization')
    queryset = Token.objects.filter(key=token)
    if queryset.exists() and len(queryset) == 1:
        return token
    return False


def paginate_items(queryset, paginator):
    queryset = paginate_items(queryset)
    
