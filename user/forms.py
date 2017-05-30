from django.contrib.auth.models import User
from django import forms


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True, label="Login")
    password = forms.CharField(widget=forms.PasswordInput, label="Hasło")

    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'email',
        )

