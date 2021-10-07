from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from api.views import feed, likes, users

api_name = 'api'

router = DefaultRouter()
router.register('users', users.UserTimelineView)

urlpatterns = [
    # url(r'^u/(?P<username>[a-z]+)/followers$', views.FollowersView.as_view(), name='followers'),
    # url(r'^u/(?P<username>[a-z]+)/follows$', views.FollowsView.as_view(), name='follows'),

    url(r'^(?P<username>[a-z]+)/unfollow$', users.unfollow_user),
    url(r'^(?P<username>[a-z]+)/follow$', users.follow_user),
    # url(r'^u/(?P<username>\w+)$', users.UserTimelineView),

    url(r'^(?P<method>(replies|conversation))/likes/create', likes.create_like),
    url(r'^replies/create', feed.create_reply),
    url(r'^conversation/create', feed.create_conversation),
    url(r'^replies', feed.get_replies),
    url(r'^conversations', feed.get_conversations)
]


urlpatterns.extend(router.urls)
