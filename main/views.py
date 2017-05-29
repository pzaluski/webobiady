import random
from datetime import date

from django.shortcuts import render

from orders.models import OrderSettings


def home(request):
    try:
        os = OrderSettings.objects.get(order_date=date.today())

        context = {
            'os': os,
            'delivery_desc': getDeliveryDesc(),
        }
    except:
        context = {
            'no_settings': 1
        }

    return render(request, "main/home.html", context)

def getDeliveryDesc():
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
    )
    d = random.choice(delivery)
    return d