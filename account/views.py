from django.shortcuts import render, redirect
from django.urls import reverse
# from django.conf import settings
from django.contrib.auth import (
        authenticate,
        login as auth_login,
        logout as auth_logout,
    )
from .forms import (
        AuthForm,
        SignupForm,
    )
# Create your views here.


def login(request):
    form = AuthForm(request, request.POST or None)
    next_url = reverse('member:member_info')
    if request.user.is_authenticated:
        return redirect(next_url)
    else:
        if request.method == 'POST' and form.is_valid():
            auth_login(request, form.get_user())
            # next_url = request.GET.get('next') or settings.LOGIN_REDIRECT_URL
            # next_url = settings.LOGIN_REDIRECT_URL
            return redirect(next_url)
        ctx = {
            'form': form,
        }
        return render(request, 'account/login.html', ctx)


def logout(request):
    if request.method == 'POST':
        auth_logout(request)
    return redirect('account:login')


def signup(request):
    form = SignupForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('account:login')
    ctx = {
        'form': form,
    }
    return render(request, 'account/signup.html', ctx)
