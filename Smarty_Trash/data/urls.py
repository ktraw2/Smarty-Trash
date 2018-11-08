from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^live', views.live, name='live'),
    url(r'^statistics/years=(?P<years>\d+)&months=(?P<months>\d+)&days=(?P<days>\d+)&hours=(?P<hours>\d+)&minutes=(?P<minutes>\d+)/$', views.statistics, name='statistics')
]
