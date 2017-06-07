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
        os.restaurant = Restaurant.objects.get(name="Zagrycha")
        os.purchaser = User.objects.get(username="mbork")
        os.order_deadline = "10:30"
        os.save()
    return os
