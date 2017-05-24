from django.contrib import admin

from .models import Order, OrderSettings

admin.site.register(Order)
admin.site.register(OrderSettings)