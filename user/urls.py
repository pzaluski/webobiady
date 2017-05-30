from django.conf.urls import url
from django.contrib.auth.views import (
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete,
)
from user import views

urlpatterns = [
    url(r'^home/$', views.home, name='user_home'),
    url(r'^register/$', views.UserRegisterView.as_view(), name='user_register'),
    url(r'^change-password/$', views.change_password, name='change_password'),
    url(r'^reset-password/$', password_reset, {'template_name': 'user/reset_password.html'}, name='reset_password'),
    url(r'^reset-password/done/$', password_reset_done, {'template_name': 'user/reset_password_done.html'}, name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', password_reset_confirm, {'template_name': 'user/reset_confirm.html'}, name='password_reset_confirm'),
    url(r'^reset-password/complete/$', password_reset_complete, {'template_name': 'user/reset_password_complete.html'}, name='password_reset_complete'),
]