from django.shortcuts import render, redirect

from .forms import ClubForm
# Create your views here.


def entry_club(request):
    club_form = ClubForm(request.POST or None)
    if request.method == 'POST' and club_form.is_valid():
        club_form.save()
        return redirect('member:member_info')
    ctx = {
        'club_form': club_form,
    }
    return render(request, 'club_entry.html', ctx)
