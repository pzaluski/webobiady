from django.shortcuts import render, render_to_response
from django.template import RequestContext
from orders.models import OrderSettings

import random
from datetime import date

def home(request):
    try:
        os = OrderSettings.objects.get(order_date=date.today())

        context = {
            'os': os,
            'delivery_desc': get_delivery(),
        }
    except:
        context = {
            'no_settings': 1
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
    )
    d = random.choice(delivery)
    return d


