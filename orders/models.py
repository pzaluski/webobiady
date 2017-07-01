from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from restaurants.models import Restaurant, Dish
from main import utils
from datetime import datetime


class OrderSettings(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, verbose_name="Restauracja")
    order_deadline = models.TimeField(verbose_name="Termin składania zamówień", default="10:30")
    purchaser = models.ForeignKey(User, related_name="purchaser", verbose_name="Kupujący")
    #order_date = models.DateField(verbose_name="Data zamówienia")
    active = models.BooleanField(default=False, verbose_name="Aktywny")

    class Meta:
        verbose_name_plural = "Ustawienia zamówień"
        verbose_name = "Ustawienia zamówień"

    def save(self, *args, **kwargs):
        super(OrderSettings, self).save(*args, **kwargs)
        if self.active:
            OrderSettings.objects.exclude(pk=self.id).update(active=False)

    def __str__(self):
        if self.active:
            is_active = '< Aktywny >'
        else:
            is_active = ''
        return '{0} {1} {2}'.format(is_active, self.restaurant.name, self.purchaser.username)


class OrdersManager(models.Manager):
    def orders_for_user(self, user, order_date):
        return super(OrdersManager, self).get_queryset().filter(
            user_id=user.id,
            date_created__year=order_date.year,
            date_created__month=order_date.month,
            date_created__day=order_date.day,
        )

    def all_orders_for_today(self):
        today = datetime.today()
        return super(OrdersManager, self).get_queryset().filter(
            settings=utils.get_order_settings(),
            date_created__year=today.year,
            date_created__month=today.month,
            date_created__day=today.day,
        )


class Order(models.Model):
    ORDER_STATUS = (
        ('NEW', 'Nowe'),
        ('ACCEPTED', 'Zamówione'),
        ('COMPLETED', 'Do odbioru'),
        ('REJECTED', 'Odrzucone'),
    )

    settings = models.ForeignKey(OrderSettings, on_delete=models.CASCADE, verbose_name="Ustawienia")
    dishes = models.ManyToManyField(Dish, default=None, verbose_name="Menu")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Cena zamówienia", default=0)
    paid = models.BooleanField(default=False, verbose_name="Zapłacono")
    date_created = models.DateField(auto_now_add=True, verbose_name="Data zamówienia")
    order_status = models.CharField(max_length=10, choices=ORDER_STATUS, default='NEW', verbose_name="Status zamówienia")
    user = models.ForeignKey(User, verbose_name="Zamawiający")
    comment = models.CharField(max_length=4000, verbose_name="Komentarz", blank=True)

    class Meta:
        verbose_name_plural = "Zamówienie"
        verbose_name = "Zamówienie"

    objects = OrdersManager()

    def get_restaurant(self):
        return self.settings.restaurant

    def get_purchaser(self):
        purchaser_name = self.settings.purchaser.username

        if self.settings.purchaser.userprofile.purchaser_name:
            purchaser_name = self.settings.purchaser.userprofile.purchaser_name

        return purchaser_name

    def get_total_price(self):
        return self.price + self.settings.restaurant.delivery_price

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
        return '{2} {0}: {1} Restauracja: {3}'.format(
            self.user.username,
            self.price,
            self.date_created,
            self.settings.restaurant.name
        )


