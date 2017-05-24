from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    menu_url = models.CharField(max_length=50)
    delivery_price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return "{}".format(self.name)

