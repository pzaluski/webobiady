from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from restaurants.models import Restaurant, Dish


class OrderSettings(models.Model):
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
        ('ACCEPTED', 'Zamówione'),
        ('COMPLETED', 'Do odbioru'),
    )
    settings = models.ForeignKey(OrderSettings, on_delete=models.CASCADE, verbose_name="Ustawienia")
    dishes = models.ManyToManyField(Dish, default=None, verbose_name="Menu")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Cena zamówienia", default=0)
    paid = models.BooleanField(default=False, verbose_name="Zapłacono")
    date_created = models.DateField(auto_now_add=True, verbose_name="Data zamówienia")
    order_status = models.CharField(max_length=10, choices=ORDER_STATUS, default='NEW', verbose_name="Status zamówienia")
    user = models.ForeignKey(User, verbose_name="Zamawiający")

    objects = OrdersManager()

    def get_restaurant(self):
        return self.settings.restaurant

    def get_dict_status_choices(self):
        d = []
        for s in self.ORDER_STATUS:
            selected = False

            if s[0] == self.order_status:
                selected = True
            d.append({'code': s[0], 'name': s[1], 'selected': selected})

        return d

    def get_delivery_price(self):
        return self.settings.restaurant.delivery_price

    def get_absolute_url(self):
        return reverse('order_update', kwargs={'pk': self.pk})

    def __str__(self):
        return '{2} {0}: {1} Restauracja: {3}'.format(self.user.username, self.price, self.settings.order_date, self.settings.restaurant.name)


