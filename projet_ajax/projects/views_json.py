#!/usr/bin/python
# -*- coding: utf8 -*-
"""JSON views for the projects application.

"""

import json
import logging

from django.contrib.auth.models import User

from django.views.generic.edit import UpdateView
from django.http import (HttpResponseRedirect,
                         HttpResponse)

from django.db.models import Q

from django.views.generic import FormView

from dal import autocomplete


from .models import Project
from .forms import ProjectChampionForm


# Get an instance of a logger
logger = logging.getLogger(__name__)


class ApiEACGetchampionsJSONView(FormView):
    """
    Documentation
    =============

    - https://ccbv.co.uk/projects/Django/1.9/django.views.generic.edit/FormView/

    """
    def get(self, request, *args, **kwargs):
        """term is sent by the jquery-ui autocomplete widget.

        The filter is on the username and the user email.

        """
        term = request.GET.get("term")
        if term:
            users = User.objects.filter(Q(username__icontains=term)
                                        | Q(email__icontains=term)).order_by('username')
        else:
            users = User.objects.all()[:50]

        results = []
        for user in users:
            user_json = {}
            user_json['id'] = user.id
            user_json['label'] = user.username
            user_json['value'] = user.username
            results.append(user_json)

        data = json.dumps(results)
        mimetype = 'application/json'
        return HttpResponse(data, mimetype)



class ApiEACGetProjectsJSONView(FormView):
    """
    Documentation
    =============

    - https://ccbv.co.uk/projects/Django/1.10/django.views.generic.edit/FormView/

    """
    def get(self, request, *args, **kwargs):
        """Return JSON records.

        """
        term = request.GET.get("term")
        if term:
            projects = Project.objects.filter(title__icontains=term)
        else:
            projects = Project.objects.all()[:50]

        results = []
        for project in projects:
            project_json = {}
            project_json['id'] = project.id
            project_json['title'] = project.title
            results.append(project_json)

        data = json.dumps(results)
        mimetype = 'application/json'
        return HttpResponse(data, mimetype)
