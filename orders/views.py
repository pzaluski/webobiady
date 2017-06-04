from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from main.utils import get_order_settings
from .forms import OrderForm
from .models import Order


@method_decorator(login_required, name='dispatch')
class DailyOrdersList(ListView):
    context_object_name = 'daily_orders'
    queryset = Order.objects.filter(settings=get_order_settings())
    template_name = 'orders/daily_orders.html'


@login_required
def new_order(request):
    os = get_order_settings()
    order = Order(user=request.user, settings=os, total_price=0)
    if request.method == 'POST':
        form = OrderForm(data=request.POST, instance=order)
        if form.is_valid():
            order = form.save(commit=False)
            order.total_price = order.price + order.settings.restaurant.delivery_price
            order.save()
            return redirect('user_home')
    else:
        form = OrderForm(instance=order)
    return render(request, "orders/new_order.html", {'form': form})
