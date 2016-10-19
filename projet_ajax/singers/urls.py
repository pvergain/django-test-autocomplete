#!/usr/bin/python
# -*- coding: utf8 -*-

from django.conf.urls import url
from  .views import (SongUpdate,
                     BookUpdate,
                     AuthorAutocomplete)


urlpatterns = [
    url(r'^song/(?P<pk>\d+)/update/$', SongUpdate.as_view(), name='song_update'),
    url(r'^book/(?P<pk>\d+)/update/$', BookUpdate.as_view(), name='book_update'),
    url(r'^author_autocomplete/$', AuthorAutocomplete.as_view(), name='author_autocomplete'),
]
