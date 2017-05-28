from django.conf.urls import url

from orders import views

urlpatterns = [
    url(r'^orderform$', views.new_order, name='order_form'),
]