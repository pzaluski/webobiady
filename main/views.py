from django.shortcuts import render
from django.http import HttpResponse

from orders.models import OrderSettings
import random
from datetime import date
from restaurants.models import Restaurant

def home(request):
    try:
        os = OrderSettings.objects.get(order_date = date.today())

        dctRender = {
            'restaurant_name': os.restaurant.name,
            'delivery_price': os.restaurant.delivery_price,
            'order_deadline': os.order_deadline,
            'menu_url': os.restaurant.menu_url,
            'delivery_desc': getDeliveryDesc(),
        }
    except:
        dctRender = {
        }

    return render(request, "main/home.html", dctRender)

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