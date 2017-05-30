from django.conf.urls import url

from user import views

urlpatterns = [
    url(r'^home$', views.home, name='user_home'),
    url(r'^register$', views.UserRegisterView.as_view(), name='user_register'),
]