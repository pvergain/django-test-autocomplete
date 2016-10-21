# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import (ProjectUpdateView,
                    ChampionAutoCompleteView,
                    ProjectAutocompleteView)


urlpatterns = [
     url(r'^project/(?P<pk>\d+)/update/$',
         ProjectUpdateView.as_view(),
         name='project_update'),

     # calls by jquery-ui autocomplete (AJAX calls)
     # http://127.0.0.1:8004/projects/champion_get_json/?term=a
     url(r'^champion_get_json/$',
         ChampionAutoCompleteView.as_view(),
         name='champion_get_json'),

     # calling example:
     # http://127.0.0.1:8004/projects/project_autocomplete/?q=a
     url(
        r'^project_autocomplete/$',
        ProjectAutocompleteView.as_view(),
        name='project_autocomplete',
     ),
]