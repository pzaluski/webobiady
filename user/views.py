from datetime import date

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

from orders.models import Order


@login_required
def home(request):
    try:
        uo = Order.objects.get(user=request.user, date_created=date.today())
        uo.sum_price = uo.total_price + uo.get_delivery_price()
    except ObjectDoesNotExist:
        return render(request, "user/home.html")
    return render(request, "user/home.html", {'uo': uo})
