from django import forms

from main import utils
from .models import Order, Dish


class OrderForm(forms.ModelForm):
    #dishes = forms.ModelMultipleChoiceField(
    #    queryset=Dish.objects.filter(restaurant=utils.get_order_settings().restaurant).order_by('name'),
    #    label="Wybierz danie",
    #    widget=forms.CheckboxSelectMultiple(attrs=({'class': 'multi'}))
    #)
    #comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}), label="Komentarz", required=False)

    def __init__(self, *args, **kwargs):
        self.order_settings = kwargs.pop('order_settings', None)
        self.destination_url = kwargs.pop('destination_url', None)
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['dishes'] = forms.ModelMultipleChoiceField(
            queryset=Dish.objects.filter(restaurant=utils.get_order_settings().restaurant).order_by('name'),
            label="Wybierz danie",
            widget=forms.CheckboxSelectMultiple(attrs=({'class': 'multi'}))
        )
        self.fields['comment'] = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}), label="Komentarz", required=False)

    class Meta:
        model = Order
        fields = ['dishes', 'comment']


class OrderPurchaserForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['order_status', 'paid']
        widgets = {
            'paid': forms.CheckboxInput()
        }
