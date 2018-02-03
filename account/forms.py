from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class AuthForm(AuthenticationForm):
    error_messages = {
        'invalid_login': 'Your id or password is wrong',
        'inactive': 'No user',
    }


class SignupForm(UserCreationForm):
    error_messages = {
        'password_mismatch': '잘못된 비밀번호입니다.',
    }
    name = forms.CharField()
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email is None:
            raise forms.ValidationError('email input error')
        return email

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name is None:
            raise forms.ValidationError('input name')
        return name

    def save(self, commit=True):
        user = super().save(commit=False)
        user.name = self.cleaned_data['name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
