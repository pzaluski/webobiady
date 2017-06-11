from django.forms import ModelForm, Textarea, NumberInput, CheckboxInput

from .models import Order


class OrderForm(ModelForm):

    class Meta:
        model = Order
        fields = ['description', 'price']
        widgets = {
            'description': Textarea(attrs={'cols': 10, 'rows': 10}),
            'price': NumberInput(attrs={'min': 0, 'step': 'any'}),
        }


class OrderPurchaserForm(ModelForm):

    class Meta:
        model = Order
        fields = ['order_status', 'paid', 'price']
        widgets = {
            'paid': CheckboxInput()
        }