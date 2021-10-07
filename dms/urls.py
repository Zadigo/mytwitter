from django.conf.urls import url

from dms import views

app_name = 'directmessages'

urlpatterns = [
    url(r'^(?P<sender>\d+)\-(?P<receiver>\d+)/send$', views.send_direct_message, name='send'),
    url(r'^(?P<sender>\d+)\-(?P<receiver>\d+)$', views.DirectMessagesView.as_view(), name='messages'),
    url(r'^$', views.HomeView.as_view(), name='home')
]
