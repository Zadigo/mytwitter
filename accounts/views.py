import datetime
import re

from django.contrib import auth, messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import add_message, error, success
from django.core.mail import BadHeaderError, send_mail
from django.http.response import (Http404, HttpResponse, HttpResponseForbidden,
                                  HttpResponseRedirect)
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _
from django.views.decorators.cache import never_cache
from django.views.generic import FormView, RedirectView, View

from accounts import models
from accounts.forms import authentication as auth_forms
from accounts.forms import profile as profile_forms

MYUSER = auth.get_user_model()

# class SignupView(View):
#     """View that helps the user create a new account"""
#     def get(self, request, *args, **kwargs):
#         context = {'consent': True, 'form': forms.UserSignupForm}
#         return render(request, 'pages/registration/signup.html', context)

#     def post(self, request, **kwargs):
#         email = request.POST['email']

#         user_exists = MYUSER.objects.filter(email__iexact=email).exists()
#         if user_exists:
#             return redirect(reverse('login'))
            
#         else:
#             form = forms.UserSignupForm(data=request.POST)
#             if form.is_valid():
#                 user = form.save()
#                 if user:
#                     email = form.cleaned_data.get('email')
#                     password = form.cleaned_data.get('password2')
#                     auth.login(request, auth.authenticate(request, email=email, password=password))
#                     return redirect(request.GET.get('next') or reverse('profile'))
#             else:
#                 return render(request, 'pages/registration/signup.html', {'form': form})


class SignupView(FormView):
    form_class = auth_forms.UserSignupForm
    template_name = 'pages/registration/signup.html'
    success_url = '/login/'

    @never_cache
    def post(self, request, *args, **kwargs):
        old_form = super().post(request, *args, **kwargs)
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = MYUSER.objects.filter(email__iexact=email)
            if user.exists():
                messages.error(request, _("Vous possédez déjà un compte chez nous"), extra_tags='alert-danger')
                return redirect('accounts:login')
            else:
                new_user = form.save()
                if new_user:
                    password = form.cleaned_data.get('password2')
                    auth.login(request, auth.authenticate(request, email=email, password=password))
                    return self.get_redirect_url(request)
        else:
            message = {
                'message': _("Une erreur est arrivée - SIG-ER"),
                'level': messages.ERROR,
                'extra_tags': 'alert-danger'
            }
        messages.add_message(request, **message)
        return old_form

    def get_redirect_url(self, request, intermediate_view=None, user=None):
        if intermediate_view is None:
            return redirect(request.GET.get('next') or reverse('accounts:profile:home'))
        if user is None:
            return Http404('User could not identified - INT-US')
        request.session['user'] = user.id
        return redirect(intermediate_view)

# class LoginView(View):
#     """View that lets the user login to his account"""
#     def get(self, request, *args, **kwargs):
#         return render(request, 'pages/registration/login.html', context={'form': forms.UserLoginForm})

#     def post(self, request, **kwargs):
#         # HACK: Even with the email field,
#         # the latter is referenced as
#         # 'username'
#         email = request.POST['username']
#         password = request.POST['password']
        
#         user = auth.authenticate(request, email=email, password=password)
#         if user:
#             auth.login(request, user)
#             return redirect(request.GET.get('next') or 'home')
#         else:
#             messages.error(request, "Nous n'avons pas pu trouver votre compte")
#             return redirect('accounts:login')


class LoginView(FormView):
    form_class = auth_forms.UserLoginForm
    template_name = 'pages/registration/login.html'
    success_url = '/'

    @never_cache
    def post(self, request, *args, **kwargs):        
        email = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(request, email=email, password=password)
        if user:
            auth.login(request, user)
            return redirect(request.GET.get('next') or 'home')
        messages.error(request, _("Nous n'avons pas pu trouver votre compte"), extra_tags='alert-danger')
        return redirect('accounts:login')

# class LogoutView(View):
#     """Logs out the user from their account"""
#     def get(self, request, *args, **kwargs):
#         auth.logout(request)
#         return redirect('home')


class LogoutView(RedirectView):
    url = '/'
    
    def get(self, request, *args, **kwargs):
        url = self.get_redirect_url(*args, **kwargs)
        auth.logout(request)
        return HttpResponseRedirect(url)


class ForgotPasswordView(View):
    """
    A single field form where the user can ask for
    a password reset
    """
    def get(self, request, *args, **kwargs):
        context = {'form': auth_forms.CustomPassowordResetForm}
        return render(request, 'pages/registration/forgot_password.html', context)

    def post(self, request, **kwargs):
        form = auth_forms.CustomPassowordResetForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']

            context = {'form': auth_forms.CustomPassowordResetForm}

            user = MYUSER.objects.filter(email__iexact=email)
            if user.exists():
                try:
                    # NOTE: Change to append a token to the url
                    # which will help iD the user in the confirm view
                    form.save(request, 'contact.mywebsite@gmail.com')
                except:
                    message = {
                        'message': _("Une erreur est arrivé - EMA-ER"),
                        'level': messages.ERROR,
                        'extra_tags': 'alert-danger'
                    }
                else:
                    message = {
                        'message': _(f"Un email a été envoyé à {email}"),
                        'level': messages.ERROR,
                        'extra_tags': 'alert-success'
                    }
            else:
                message = {
                    'message': _("Nous n'avons pas pu vous trouvez votre addresse mail"),
                    'level': messages.ERROR,
                    'extra_tags': 'alert-danger'
                }

            messages.add_message(request, **message)
            return render(request, 'pages/registration/forgot_password.html', context=context)

        return redirect('accounts:login')


class UnauthenticatedPasswordResetView(View):
    """
    Helps a non authenticated user reset his password
    """
    def get(self, request, *args, **kwargs):
        # user_token = request.GET.get('user_token')
        # if not user_token:
        #     return HttpResponseForbidden(reason='Missing argument')
        
        context = {
            'form': auth_forms.CustomSetPasswordForm(MYUSER.objects.get(id=1)),
        }
        return render(request, 'pages/registration/forgot_password_confirm.html', context)

    def post(self, request, **kwargs):
        # user_token = request.GET.get('user_token')
        # user = get_object_or_404(MYUSER, id=user_token)
        form = auth_forms.CustomSetPasswordForm(user)
        if form.is_valid():
            form.save()
        auth.login(request, user)
        return redirect('profile')
