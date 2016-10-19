#!/usr/bin/python
# -*- coding: utf8 -*-
"""projet_ajax URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls import (include,
                              url)

from django.contrib import admin

from ajax_select import urls as ajax_select_urls
from singers import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^search',
        view=views.search_form,
        name='search_form'),
    url(r'^admin/lookups/', include(ajax_select_urls)),

    url(r'^projects/', include('projects.urls', namespace='projects')),
    url(r'^singers/', include('singers.urls', namespace='singers')),
]


if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    from django.conf.urls.static import static
    urlpatterns += staticfiles_urlpatterns()
    # voir p.405 "Django By Example"
    # https://docs.djangoproject.com/en/dev/howto/static-files/#serving-files-uploaded-by-a-user-during-development
    urlpatterns += static(settings.MEDIA_URL ,
                          document_root=settings.MEDIA_ROOT)

    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]