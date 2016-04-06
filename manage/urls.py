from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'stat/',views.CheckState.as_view(), name='check_stat'),
    url(r'pingstate/',views.CheckPing.as_view(), name="check_ping"),
    url(r'sendgit',views.SendGit.as_view(),name="send_git"),
]
