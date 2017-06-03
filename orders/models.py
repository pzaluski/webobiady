from datetime import datetime

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models

from restaurants.models import Restaurant


class OrderSettings(models.Model):
    def_time = datetime.now().replace(hour=10, minute=30, second=0, microsecond=0)

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    order_deadline = models.TimeField(verbose_name="Termin składania zamówień", default="10:30")
    purchaser = models.ForeignKey(User, related_name="purchaser", verbose_name="Kupujący")
    order_date = models.DateField()

    def __str__(self):
        return '{0} - {1}'.format(self.order_date.strftime("%d.%m.%Y"), self.restaurant.name)


class OrdersManager(models.Manager):
    def orders_for_user(self, user, order_date):
        return super(OrdersManager, self).get_queryset().filter(user_id=user.id, settings__order_date=order_date)


class Order(models.Model):
    ORDER_STATUS = (
        ('NEW', 'Nowe'),
        ('SENT', 'Wysłane'),
        ('ACCEPTED', 'Przyjęte'),
    )
    settings = models.ForeignKey(OrderSettings, on_delete=models.CASCADE)
    description = models.CharField(max_length=400, verbose_name="Nazwa dania")
    price = models.DecimalField(
                                max_digits=10,
                                decimal_places=2,
                                verbose_name="Cena zamówienia bez dostawy",
                                validators=[MinValueValidator(0)]
                                )
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Cena z dostawą")
    paid = models.BooleanField(default=False, verbose_name="Zapłacono")
    date_created = models.DateField(auto_now_add=True, verbose_name="Data zamówienia")
    order_status = models.CharField(max_length=10, choices=ORDER_STATUS, default='NEW', verbose_name="Status zamówienia")
    user = models.ForeignKey(User, verbose_name="Zamawiający")

    objects = OrdersManager()

    def __str__(self):
        return '{0} {1}: {2} {3}'.format(self.user.first_name, self.user.last_name, self.description, self.total_price)


