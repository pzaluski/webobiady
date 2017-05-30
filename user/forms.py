from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, label="Imię")
    last_name = forms.CharField(required=True, label="Nazwisko")

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
        )

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.username = user.first_name[0:1].lower() + user.last_name.lower()
        if commit:
            user.save()

        return user


