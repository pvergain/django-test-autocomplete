#!/usr/bin/python
# -*- coding: utf8 -*-

from django.conf.urls import url
from  .views import SongUpdate


urlpatterns = [
    url(r'^song/(?P<pk>\d+)/update/$', SongUpdate.as_view(), name='song_update')
]
