from django.forms import ModelForm, Textarea, NumberInput

from .models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['description', 'price']
        widgets = {
            'description': Textarea(attrs={'cols': 10, 'rows': 10}),
            'price': NumberInput(attrs={'step': 0.50}),
        }
