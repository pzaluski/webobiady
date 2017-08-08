from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    menu_url = models.CharField(max_length=400)
    delivery_price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name_plural = "Restauracja"
        verbose_name = "Restauracja"

    def get_menu(self):
        return Dish.objects.dishes_for_restaurant(self)

    def __str__(self):
        return "{}".format(self.name)


class DishesManager(models.Manager):
    def dishes_for_restaurant(self, restaurant):
        return super(DishesManager, self).get_queryset().filter(restaurant=restaurant)


class Dish(models.Model):
    name = models.CharField(max_length=400)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Danie"
        verbose_name = "Danie"

    objects = DishesManager()

    def __str__(self):
        return "{0} - {1}".format(self.name, self.price)



