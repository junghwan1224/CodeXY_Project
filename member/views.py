from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.db.models import Q

from club.models import Club
from .forms import ProfileForm
# Create your views here.


def member_info(request):
    ctx = {
        'member': settings.AUTH_USER_MODEL,
        'search_result': search(request)[1],
        'q': search(request)[0],
    }
    return render(request, 'main.html', ctx)


@login_required
def edit_profile(request):
    try:
        profile_form = ProfileForm(request.POST or None, instance=request.user.profile)
    except:  # 예외처리 에러 몰라서 작성 안함
        profile_form = ProfileForm(request.POST or None)
    if request.method == 'POST' and profile_form.is_valid():
        profile = profile_form.save(commit=False)
        profile.user = request.user
        profile.save()
        return redirect('member:member_info')
    ctx = {
        'profile_form': profile_form,
    }
    return render(request, 'profile_edit.html', ctx)


def search(request):
    search_text = request.GET.get('q', '')
    if search_text:
        club_result = Club.objects.filter(club_name__icontains=search_text)
        return (search_text, club_result)
    else:
        club_result = None
        return (search_text, club_result)


@login_required
def apply(request, club):
    pass
