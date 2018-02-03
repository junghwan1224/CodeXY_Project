from django import forms
from django.contrib.auth.models import User
from .models import Profile


class MemberForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('club', 'user', )
