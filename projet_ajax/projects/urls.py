# -*- coding: utf-8 -*-

from django.conf.urls import url

urlpatterns = [
     url(r'^add/$', 'add'),
     url(r'^champion_auto_complete/$',
         'champion_auto_complete', name='champion_auto_complete'),
]