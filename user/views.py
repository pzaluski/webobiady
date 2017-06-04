from datetime import date

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from orders.models import Order


@login_required
def home(request):
    uo = Order.objects.orders_for_user(user=request.user, order_date=date.today())
    return render(request, "user/home.html", {'uo': uo})
