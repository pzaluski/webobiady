from datetime import date

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import OrderForm
from .models import Order, OrderSettings


@login_required
def new_order(request):
    try:
        os = OrderSettings.objects.get(order_date=date.today())
        order = Order(user=request.user, settings=os, total_price=0)
    except:
        return render(request, "orders/new_order.html", {'form': OrderForm(), 'no_settings': 1})
    if request.method == 'POST':
        form = OrderForm(data=request.POST, instance=order)
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.total_price = new_order.price + new_order.settings.restaurant.delivery_price
            new_order.save()
            return redirect('user_home')
    else:
        form = OrderForm(instance=order)
    return render(request, "orders/new_order.html", {'form': form})