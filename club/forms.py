from django import forms

from .models import Club


class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        exclude = ('position', )

    def save(self, commit=True):
        club = super().save(commit=False)
        club.position = True
        if commit:
            club.save()
        return club
