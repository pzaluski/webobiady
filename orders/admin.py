from django.contrib import admin

from .models import Order, OrderSettings


class OrderSettingsModelAdmin(admin.ModelAdmin):
    list_display = ["restaurant", "purchaser", "active"]
    list_filter = ["restaurant", "active"]


class OrderModelAdmin(admin.ModelAdmin):
    list_display = ["__str__", "date_created", "paid"]
    list_filter = ["date_created", "paid", "user", "settings"]
    list_editable = ["paid"]

    class Meta:
        model = Order

admin.site.register(Order, OrderModelAdmin)
admin.site.register(OrderSettings, OrderSettingsModelAdmin)
