from django.conf.urls import url
from restaurants import views

urlpatterns = [
    url(r'^import_menu$', views.import_menu, name='import_menu'),
]