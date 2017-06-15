from django import forms

from main import utils
from .models import Order, Dish


class OrderForm(forms.ModelForm):
    dishes = forms.ModelMultipleChoiceField(
        queryset=Dish.objects.filter(restaurant=utils.get_today_restaurant()),
        label="Wybierz danie",
        widget=forms.CheckboxSelectMultiple(attrs=({'class': 'multi'}))
    )

    class Meta:
        model = Order
        fields = ['dishes']


class OrderPurchaserForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['order_status', 'paid']
        widgets = {
            'paid': forms.CheckboxInput()
        }