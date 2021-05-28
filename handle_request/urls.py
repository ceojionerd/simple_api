from functools import partial
from django.conf.urls import url
from .api import UUIDList
from .views import home

urlpatterns = [
    url('json/', home, name="home"),
    url(r'^api/uuid_list/$', UUIDList.as_view(), name='uuid_list')
]