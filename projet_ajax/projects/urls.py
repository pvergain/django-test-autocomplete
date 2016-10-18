# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import ProjectUpdateView

urlpatterns = [
     url(r'^project/(?P<pk>\d+)/update/$',
         ProjectUpdateView.as_view(),
         name='project_update'),

     # calls by jquery-ui autocomplete (AJAX calls)
     url(r'^champion_auto_complete/$',
         'champion_auto_complete',
         name='champion_auto_complete'),
]