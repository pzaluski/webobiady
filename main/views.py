import random

from django.shortcuts import render

from .utils import get_order_settings


def home(request):
    purchaser = False
    os = get_order_settings()
    if request.user.is_authenticated() and request.user == os.purchaser:
        purchaser = True

    menu = os.restaurant.get_menu()

    context = {
        'os': os,
        'purchaser': purchaser,
        'delivery_desc': get_delivery(),
        'menu': menu,
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


