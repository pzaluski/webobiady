from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

from main.utils import get_order_settings
from orders.models import Order


@login_required
def home(request):
    edit = False
    try:
        os = get_order_settings()
        now = datetime.now().time()
        print(now, os.order_deadline, now > os.order_deadline)
        if now < os.order_deadline:
            edit = True
        uo = Order.objects.get(user=request.user, settings=os)
        uo.total_price = uo.price + uo.get_delivery_price()
    except ObjectDoesNotExist:
        return render(request, "user/home.html")
    return render(request, "user/home.html", {'uo': uo, 'edit': edit})
