from django.conf.urls import url

from user import views

urlpatterns = [
    url(r'^home/$', views.home, name='user_home'),
]
