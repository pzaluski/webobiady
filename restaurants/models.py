from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    menu_url = models.CharField(max_length=50)
    delivery_price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return "{}".format(self.name)


class Category(models.Model):
    name = models.CharField(max_length=400)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.name)


class Dish(models.Model):
    name = models.CharField(max_length=400)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, default=None)

    def __str__(self):
        return "{0} - {1}".format(self.name, self.price)



