from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings

from .models import Profile
# Create your views here.


@login_required
def member_info(request):
    return render(request, 'member_info.html')
