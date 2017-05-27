from django.db import models
from django.contrib.auth.models import User
from restaurants.models import Restaurant


class OrderSettings(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    order_deadline = models.TimeField()
    purchaser = models.ForeignKey(User, related_name="purchaser")
    order_date = models.DateField()

    def __str__(self):
        return '{0} - {1}'.format(self.order_date.strftime("%d.%m.%Y"), self.restaurant.name)

class Order(models.Model):
    ORDER_STATUS = (
        ('NEW', 'Nowe'),
        ('SENT', 'Wysłane'),
        ('ACCEPTED', 'Przyjęte'),
    )
    settings = models.ForeignKey(OrderSettings, on_delete=models.CASCADE)
    description = models.CharField(max_length=400)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField()
    date_created = models.DateField(auto_now_add=True)
    order_status = models.CharField(max_length=10, choices=ORDER_STATUS)
    user = models.ForeignKey(User)

    def __str__(self):
        return '{0} {1}: {2} {3}'.format(self.user.first_name, self.user.last_name, self.description, self.total_price)
