from django.contrib import admin

from .models import Restaurant, Dish


class DishModelAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "restaurant"]
    list_filter = ["restaurant"]

    class Meta:
        model = Dish

admin.site.register(Restaurant)
admin.site.register(Dish, DishModelAdmin)
