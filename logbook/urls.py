from django.conf.urls import include, url
from views import *

urlpatterns = [
    url(r'^$', Logbook.as_view(), name='logbook'),
    url(r'^firma/$', firma, name='firma')
]