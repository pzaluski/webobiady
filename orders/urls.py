from django.conf.urls import url

from orders import views

urlpatterns = [
    url(r'^order/add/$', views.OrderCreate.as_view(), name='order_form'),
    url(r'^order/(?P<pk>[0-9]+)/$', views.OrderUpdate.as_view(), name='order_update'),
    url(r'^order/(?P<pk>[0-9]+)/delete/$', views.OrderDelete.as_view(), name='order_delete'),
    url(r'^daily/orders/$', views.PurchaserOrdersList.as_view(), name='daily_orders'),
    url(r'^order/(?P<pk>[0-9]+)/edit/purchaser/$', views.PurchaserOrderEdit.as_view(), name='order_edit'),
    url(r'^order/history/(?P<year>[0-9]{4})/(?P<month>[0-9]+)/$', views.OrderArchiveMonthView.as_view(), name='order_history'),
    url(r'^message/collect/$', views.MessageCollectView.as_view(), name='message_collect'),
    url(r'^message/sent/$', views.message_sent, name='message_sent'),
]