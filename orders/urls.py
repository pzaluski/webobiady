from django.conf.urls import url
from orders import views

urlpatterns = [
    url(r'^order/add/$', views.OrderCreate.as_view(), name='order_form'),
    url(r'^order/(?P<pk>[0-9]+)/$', views.OrderUpdate.as_view(), name='order_update'),
    url(r'^order/(?P<pk>[0-9]+)/delete/$', views.OrderDelete.as_view(), name='order_delete'),
    #url(r'^order/edit/$', views.OrderPurchaserEdit.as_view(), name='order_edit'),

    url(r'^daily_orders/$', views.OrderPurchaserEdit.as_view(), name='daily_orders'),
    url(r'^(?P<pk>[0-9]+)/$', views.OrderDetail.as_view(), name='order_details'),
]