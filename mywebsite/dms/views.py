import json

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.html import mark_safe
from django.views.decorators.http import require_POST
from django.views.generic import View, ListView, TemplateView

from dms import models

MYUSER = get_user_model()


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/direct_messages.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = models.DirectMessage.messages_manager.my_messages(self.request.user)
        list_of_users = queryset.values_list('message_receiver__username', flat=True)
        context['list_of_users'] = set(user for user in list(list_of_users) if user != self.request.user.username)
        return context

class DirectMessagesView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        current_user = MYUSER.objects.get(id=self.request.user.id)
        receiver = MYUSER.objects.get(id=kwargs['receiver'])

        queryset = models.DirectMessage.messages_manager.my_messages(current_user)
        list_of_users = queryset.values_list('message_receiver__username', flat=True)
        
        context = {
            'test_something': json.dumps('[{"test": "great"}]'),

            'receiver': receiver,
            'messages': queryset,
            'messages_with_user': models.DirectMessage.messages_manager
                                            .messages_with_specific_user(current_user, receiver, queryset=queryset),
            'receivers': set(user for user in list(list_of_users) if user != request.user.username)
        }
        return render(request, 'pages/direct_messages.html', context)
        

@login_required
@require_POST
def send_direct_message(request, **kwargs):
    sender = MYUSER.objects.get(id=request.user.id)
    receiver = MYUSER.objects.get(id=kwargs['receiver'])
    data = {
        'message_sender': sender,
        'message_receiver': receiver,
        'text': json.loads(request.body)['text']
    }
    new_message = models.DirectMessage.objects.create(**data)
    return JsonResponse(data={'state': True, 'text': new_message.text})
