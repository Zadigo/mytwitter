from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from api.views import feed, likes, users, authentication

api_name = 'api'

router = DefaultRouter()
router.register('users', users.UsersView)

urlpatterns = [
    # url(r'^u/(?P<username>[a-z]+)/followers$', views.FollowersView.as_view(), name='followers'),
    # url(r'^u/(?P<username>[a-z]+)/follows$', views.FollowsView.as_view(), name='follows'),

    url(r'^auth/refresh', authentication.logout_view),
    url(r'^auth/token', authentication.login_view),

    url(r'^(?P<username>[a-z]+)/unfollow$', users.unfollow_user),
    url(r'^(?P<username>[a-z]+)/follow$', users.follow_user),

    url(r'^(?P<method>(replies|conversations))/(?P<pk>\d+)/vote', likes.create_like),
    url(r'^conversations/(?P<pk>\d+)/replies/create', feed.create_reply),
    url(r'^conversations/create', feed.create_conversation),
    url(r'^conversations/(?P<pk>\d+)/replies', feed.get_replies),
    url(r'^conversations', feed.get_conversations)
]


urlpatterns.extend(router.urls)
