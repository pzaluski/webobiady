from django import forms

from .models import Restaurant


class ImportMenuForm(forms.Form):
    restaurant = forms.ModelChoiceField(queryset=Restaurant.objects.all(), empty_label=None, label="Restauracja")
    menu_html_src = forms.CharField(widget=forms.Textarea, label="Żródło strony z menu")

