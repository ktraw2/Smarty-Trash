from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^livedata', views.livedata, name='getdata'),
    url(r'^statistics/years=(?P<years>\d+)&months=(?P<months>\d+)&days=(?P<days>\d+)&hours=(?P<hours>\d+)&minutes=(?P<minutes>\d+)/$', views.statistics, name='statistics')
]
