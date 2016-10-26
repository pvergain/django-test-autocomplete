# -*- coding: utf-8 -*-

from django.conf.urls import url


from .views_json import (ApiEACGetProjectsJSONView,
                        ApiEACGetchampionsJSONView)

from .views_django_autocomplete_light import (ApiUserDjangoAutocompleteLight,
                                              ProjectDjangoAutoCompleteUpdateView,
                                              ProjectAutocompleteView)

from .views import (ProjectUpdateView,
                    ProjectUpdateViewEasyAutoComplete,
                    ProjectUpdateViewJQueryUIAutoComplete)


urlpatterns = [
     url(r'^project/(?P<pk>\d+)/update/$',
         ProjectUpdateView.as_view(),
         name='project_update'),

    url(r'^project/(?P<pk>\d+)/updateeasy/$',
        ProjectUpdateViewEasyAutoComplete.as_view(),
        name='project_update_easy'),

    url(r'^project/(?P<pk>\d+)/update_jquery_ui/$',
        ProjectUpdateViewJQueryUIAutoComplete.as_view(),
        name='project_update_jquery_ui'),

    url(r'^project/(?P<pk>\d+)/update_django_autocomplete/$',
        ProjectDjangoAutoCompleteUpdateView.as_view(),
        name='project_update_django_autocomplete'),

     # calls by jquery EasyAutocomplete
     # http://127.0.0.1:8004/projects/api_get_champions/?term=a
     url(r'^api_get_champions/$',
         ApiEACGetchampionsJSONView.as_view(),
         name='api_get_champions'),

    # calls by jquery EasyAutocomplete (EAC)
    # http://127.0.0.1:8004/projects/api_get_projects/?term=a
    url(r'^apis_get_projects/$',
        ApiEACGetProjectsJSONView.as_view(),
        name='api_get_projects'),

     # calling example:
     # http://127.0.0.1:8004/projects/project_autocomplete/?q=a
     url(
        r'^project_autocomplete/$',
        ProjectAutocompleteView.as_view(),
        name='project_autocomplete',
     ),

    url(r'^api/get_users/$',
        ApiUserDjangoAutocompleteLight.as_view(),
        name='api_get_users'),
]