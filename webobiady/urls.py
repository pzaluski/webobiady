"""webobiady URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import (
    url, include
)
from django.contrib import admin
from django.views.defaults import page_not_found, bad_request, permission_denied, server_error

from main import views as main_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main_views.home, name='webobiady_home'),
    url(r'^orders/', include('orders.urls')),
    url(r'^restaurants/', include('restaurants.urls')),
    url(r'^user/', include('user.urls')),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
]


handler400 = bad_request
handler403 = permission_denied
handler404 = page_not_found
handler500 = server_error
