from datetime import datetime

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from orders.models import OrderSettings
from restaurants.models import Restaurant


def get_order_settings():
    try:
        os = OrderSettings.objects.get(order_date=datetime.now())
    except ObjectDoesNotExist:
        os = OrderSettings()
        try:
            os.restaurant = Restaurant.objects.first()
        except ObjectDoesNotExist:
            r = Restaurant(name="Zagrycha", delivery_price=0)
            r.save()
            os.restaurant = r
        try:
            os.purchaser = User.objects.get(username="mbork")
        except ObjectDoesNotExist:
            os.purchaser = User.objects.first()
        os.order_deadline = "10:30"
        os.order_date = datetime.now()
        os.save()
    return os


def get_today_restaurant():
    os = get_order_settings()
    return os.restaurant
