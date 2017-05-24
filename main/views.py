from django.shortcuts import render
from django.http import HttpResponse

import random

def home(request):
    dctRender = {
        'restaurant_name': 'Trafico',
        'delivery_price': 1,
        'order_final_hour': '11:00',
        'menu_url':'http://trafico.pl',
        'delivery_desc':getTerminDostawy(),
    }
    return render(request, "main/home.html", dctRender)

def getTerminDostawy():
    tupTermin = (
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
    termin = random.choice(tupTermin)
    return termin