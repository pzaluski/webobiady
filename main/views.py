import random

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from orders.models import Order
from .utils import get_order_settings
from datetime import datetime


def home(request):
    purchaser = False
    os = get_order_settings()
    user_order = None
    if request.user.is_authenticated():
        if request.user == os.purchaser:
            purchaser = True
        try:
            user_order = Order.objects.get(
                user_id=request.user.id,
                date_created__year=datetime.today().year,
                date_created__month=datetime.today().month,
                date_created__day=datetime.today().day,
            )
        except ObjectDoesNotExist:
            pass

    menu = os.restaurant.get_menu()

    context = {
        'os': os,
        'purchaser': purchaser,
        'delivery_desc': get_delivery(),
        'menu': menu,
        'user_order': user_order
    }
    return render(request, "main/home.html", context)


def get_delivery():
    delivery = (
        'już zjedzone',
        'będzie dzisiaj',
        'jak najszybciej',
        'pracuj tam!',
        'chciałbyś wiedzieć, co?',
        'w dniu dzisiejszym',
        'kiedyś będzie',
        'nie bądź taki dociekliwy',
        'sio wścibolu',
        'jak przyjedzie to będzie',
        'maruda!',
        '..nie ględź..',
        'cierpliwości!'
    )
    d = random.choice(delivery)
    return d


