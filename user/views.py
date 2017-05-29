from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from orders.models import Order
from datetime import date


@login_required
def home(request):
    uo_all = Order.objects.filter(user__username=request.user)
    uo_prev = uo_all.exclude(settings__order_date__gte=date.today())
    uo = uo_all.filter(settings__order_date__gte=date.today())
    return render(request, "user/home.html", {'uo': uo, 'uo_prev': uo_prev})
