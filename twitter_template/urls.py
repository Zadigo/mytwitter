from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from accounts.admin import custom_site
from django.urls import path, include

urlpatterns = [
    url('', include('social_django.urls', namespace='social')),
    
    path('api/v1/', include('api.urls')),
    path('messages/', include('dms.urls')),
    path('feed/', include('feed.urls')),
    path('accounts/', include('accounts.urls')),
    # path('admin/', admin.site.urls),
    path('admin/', custom_site.urls),
    path('', include('hero.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
