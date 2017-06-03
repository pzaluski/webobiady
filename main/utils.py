from datetime import date

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from orders.models import OrderSettings
from restaurants.models import Restaurant


def get_order_settings(order_date=date.today()):
    try:
        os = OrderSettings.objects.get(order_date=order_date)
    except ObjectDoesNotExist:
        os = OrderSettings()
        os.order_date = order_date
        os.restaurant = Restaurant.objects.get(name="Zagrycha")
        os.purchaser = User.objects.get(username="palmira")
        os.order_deadline = "10:30"
        os.save()
    return os