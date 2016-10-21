# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import (ProjectUpdateView,
                    ApiGetchampionsView,
                    ProjectAutocompleteView)


urlpatterns = [
     url(r'^project/(?P<pk>\d+)/update/$',
         ProjectUpdateView.as_view(),
         name='project_update'),

     # calls by jquery-ui autocomplete (AJAX calls)
     # http://127.0.0.1:8004/projects/api_get_champions/?term=a
     url(r'^api_get_champions/$',
         ApiGetchampionsView.as_view(),
         name='api_get_champions'),

     # calling example:
     # http://127.0.0.1:8004/projects/project_autocomplete/?q=a
     url(
        r'^project_autocomplete/$',
        ProjectAutocompleteView.as_view(),
        name='project_autocomplete',
     ),
]