import json
import re

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.http.response import JsonResponse, Http404
from django.shortcuts import redirect, render, reverse
from django.views.decorators.http import require_POST, require_GET
from django.views.generic import ListView, TemplateView, View, DetailView

from feed import models

MYUSER = get_user_model()

def parse_users(text):
    has_users = re.match(r'\@([a-z]+)\s?', text)
    if has_users:
        users = has_users.groups()
        return MYUSER.objects.filter(username__in=list(users))
    return None


class TimeLineView(LoginRequiredMixin, ListView):
    model = models.Conversation
    template_name = 'pages/feed.html'
    context_object_name = 'conversations'

    def get_queryset(self):
        user = self.request.user
        follows_ids = list(user.myuserprofile.follows.values_list('id', flat=True))
        follows_ids.append(user.id)
        # queryset = self.model.objects.filter(created_by__id__in=follows_ids)
        # return queryset
        return self.model.conversations_manager.annoted_conversations(user.username, follows_ids=follows_ids)


class CustomDetailView(DetailView):
    model = MYUSER
    queryset = MYUSER.objects.all()
    context_object_name = 'user_feed'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()

        username = self.kwargs.get('username')
        if username is not None:
            queryset = queryset.filter(username__iexact=username)
            try:
                user_timeline_to_view = queryset.get()
            except:
                raise Http404(f"The following user '{username}' could not be found")
            return user_timeline_to_view
        else:
            raise AttributeError('CustomDetailView should be called with a username in the url parameters')


class UserTimeLine(LoginRequiredMixin, CustomDetailView):
    template_name = 'pages/user_feed.html'


class FollowersView(LoginRequiredMixin, CustomDetailView):
    template_name = 'pages/followers.html'


class FollowsView(LoginRequiredMixin, CustomDetailView):
    template_name = 'pages/follows.html'


class SearchView(LoginRequiredMixin, ListView):
    model = models.Conversation
    template_name = 'pages/search.html'
    context_object_name = 'conversations'

    def get_queryset(self):
        q = self.request.GET.get('q')
        return self.model.conversations_manager.search(q)


@login_required
@require_POST
def add_conversation(request, **kwargs):
    data = json.loads(request.body)
    conversation_text = data['text']
    new_conversation = models.Conversation.objects.create(
        body=conversation_text, created_by=request.user)
    messages.add_message(request, messages.SUCCESS, "Tweet created", extra_tags='alert-success')
    return JsonResponse(data={'state': True, 'creation_date': 'new_conversation.created_on'})


@login_required
@require_GET
def follow_user(request, **kwargs):
    username = kwargs['username']
    if username is not None:
        pass
    user_to_follow = MYUSER.objects.get(username__iexact=username)
    current_user = MYUSER.objects.get(username__iexact=request.user.username)
    current_user.myuserprofile.follows.add(user_to_follow.myuserprofile)
    return redirect(reverse('feed:user_timeline', args=[current_user.username]))


@login_required
@require_GET
def unfollow_user(request, **kwargs):
    username = kwargs['username']
    if username is not None:
        pass
    user_to_unfollow = MYUSER.objects.get(username__iexact=username)
    current_user = MYUSER.objects.get(username__iexact=request.user.username)
    current_user.myuserprofile.follows.remove(user_to_unfollow.myuserprofile)
    return redirect(reverse('feed:user_timeline', args=[current_user.username]))


@login_required
@require_POST
def add_like(request):
    data = json.loads(request.body)
    try:
        conversation = models.Conversation.objects.get(id=data['id'])
    except:
        return JsonResponse(data={'state': False})

    action = 'liked'

    likes = conversation.like_set.filter(user=request.user)
    if likes.exists():
        action = 'unliked'
        conversation.like_set.filter(user=request.user).delete()
    else:
        conversation.like_set.create(user=request.user)
    return JsonResponse(data={'state': True, 'action': action, 'total_likes': conversation.like_set.all().count()})


@login_required
@require_POST
def share(request):
    pass


@login_required
@require_POST
def answer_to_conversation(request):
    data = json.loads(request.body)
    conversation_text = data['text']
    users = parse_users(conversation_text)
    
    messages.add_message(request, messages.SUCCESS, "Tweet created", extra_tags='alert-success')
    return JsonResponse(data={'state': True, 'creation_date': 'new_conversation.created_on'})




@login_required
@require_POST
def delete(request):
    pass


@login_required
@require_POST
def embed(request):
    pass


@login_required
@require_POST
def send_direct_message(request):
    pass
