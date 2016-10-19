# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import (ProjectUpdateView,
                    ChampionAutoCompleteView)


urlpatterns = [
     url(r'^project/(?P<pk>\d+)/update/$',
         ProjectUpdateView.as_view(),
         name='project_update'),

     # calls by jquery-ui autocomplete (AJAX calls)
     url(r'^champion_get_json/$',
         ChampionAutoCompleteView.as_view(),
         name='champion_get_json'),
]