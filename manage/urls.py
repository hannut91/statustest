"""status URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'stat/',views.CheckState.as_view(), name='check_stat'),
    url(r'^checkversion=(?P<useros>[a-z]{1,})$', views.check_version, name='check_version'),
    url(r'^notice/(?P<useros>[a-z]{1,})/(?P<locale>[a-z]{1,})', views.check_notice, name='check_notice'),
    url(r'^maintenance/(?P<useros>[a-z]{1,})',views.check_maintenance, name='check_maintenance'),
    url(r'pingstate/',views.CheckPing.as_view(), name="check_ping"),
]
