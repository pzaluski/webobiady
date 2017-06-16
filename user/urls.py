from django.conf.urls import url

from user import views

urlpatterns = [
    url(r'^home/$', views.home, name='user_home'),
    url(r'^purchaser/(?P<pk>[0-9]+)/edit/$', views.PurchaserEditView.as_view(), name='purchaser_edit'),
]
