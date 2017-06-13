from django.forms import ModelForm, CheckboxInput

from .models import Order


class OrderForm(ModelForm):
    #dishes = ModelMultipleChoiceField(queryset=Order.dishes)

    class Meta:
        model = Order
        fields = ['dishes']


class OrderPurchaserForm(ModelForm):

    class Meta:
        model = Order
        fields = ['order_status', 'paid']
        widgets = {
            'paid': CheckboxInput()
        }