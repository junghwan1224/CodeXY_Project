from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.conf import settings
from django.db.models import Q

from .models import Club
from member.models import Member
from .forms import ClubForm
# Create your views here.


@login_required
def entry_club(request):
    club_form = ClubForm(request.POST or None)
    if request.method == 'POST' and club_form.is_valid():
        club_form.save()
        member = Member.objects.create(
                club=club_form.instance,
                member=request.user.profile,
            )
        member.save()
        return redirect('member:member_info')
    ctx = {
        'club_form': club_form,
    }
    return render(request, 'club_entry.html', ctx)


@login_required
def admin_club(request, pk):
    member = Member.objects.filter(Q(member__pk=pk, club__position=True))
    ctx = {
        'club_list': member,
    }
    return render(request, 'admin_club.html', ctx)


@login_required
def as_member_club(request, pk):
    member = Member.objects.filter(Q(member__pk=pk, club__position=False))
    ctx = {
        'club_list': member,
    }
    return render(request, 'as_member_club.html', ctx)
