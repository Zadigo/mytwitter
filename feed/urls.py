from django.conf.urls import url

from feed import views

app_name = 'feed'

urlpatterns = [
    url(r'^add-comment$', views.answer_to_conversation, name='comment'),
    url(r'^add-conversation$', views.add_conversation, name='add'),
    url(r'^add-like$', views.add_like, name='like'),
    
    url(r'^u/(?P<username>[a-z]+)/followers$', views.FollowersView.as_view(), name='followers'),
    url(r'^u/(?P<username>[a-z]+)/follows$', views.FollowsView.as_view(), name='follows'),

    url(r'^u/(?P<username>[a-z]+)/unfollow$', views.unfollow_user, name='unfollow'),
    url(r'^u/(?P<username>[a-z]+)/follow$', views.follow_user, name='follow'),
    url(r'^u/(?P<username>\w+)$', views.UserTimeLine.as_view(), name='user_timeline'),
    url(r'^search$', views.SearchView.as_view(), name='search'),
    url(r'^home$', views.TimeLineView.as_view(), name='home'),
    
    url(r'^$', views.index, name='my_feed')
]
