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
    url, include, handler400, handler403, handler404, handler500
)

from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.defaults import page_not_found

from main import views as main_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main_views.home, name='webobiady_home'),
    url(r'^orders/', include('orders.urls')),
    url(r'^user/', include('user.urls')),
]

# auth urls
urlpatterns += [
    url(r'^login/$', auth_views.login,
        {'template_name': 'login.html'},
        name='webobiady_login'),

    url(r'^logout/$', auth_views.logout,
        {'next_page': 'webobiady_home'},
        name='webobiady_logout'),

]


#handler400 = main_views.bad_request
#handler403 = main_views.permission_denied
handler404 = page_not_found
#handler500 = main_views.handler500

