from datetime import date

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from main.utils import get_order_settings
from orders.models import Order


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    collect_place = models.CharField(max_length=50, verbose_name="Miejsce odbioru", blank=True)
    purchaser_name = models.CharField(max_length=400, verbose_name="Zamawiający - nazwa", blank=True)
    purchaser_message = models.CharField(max_length=400, verbose_name="Informacja od zamawiającego", blank=True)

    def is_purchaser(self):
        os = get_order_settings()
        if os.purchaser == self.user:
            return True
        return False

    def get_orders_num(self):
        cnt = Order.objects.orders_for_user(user=self.user, order_date=date.today()).count()
        return cnt

    def __str__(self):
        if self.is_purchaser():
            p = 'Tak'
        else:
            p = 'Nie'
        return 'Zamawiający: {0} Ilość zamówień: {1}'.format(p, self.get_orders_num())


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile, new = UserProfile.objects.get_or_create(user=instance)

