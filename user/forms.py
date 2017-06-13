from django import forms
from django.contrib.auth.models import User

from .models import UserProfile


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True, label="Login")
    password = forms.CharField(widget=forms.PasswordInput, label="Hasło")
    first_name = forms.CharField(required=True, label="Imię")

    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'first_name',
            'email',
        )


class ProfileEditForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('is_purchaser',)

