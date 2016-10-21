
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


class ProjectUpdateView(UpdateView):
    """
            url(r'^projects/project/(?P<pk>\d+)/update/$', ProjctUpdate.as_view(), name='project_update'),

    Documentation:

    - http://ccbv.co.uk/projects/Django/1.10/django.views.generic.edit/UpdateView/

    """
    model = Project
    form_class = ProjectChampionForm
    context_object_name = 'project'
    template_name = 'projects/project/update_easy_simple.html'

    def get_object(self, queryset=None):
        """Pour mémoriser self.demande_article"""
        self.object = super(ProjectUpdateView, self).get_object(queryset)
        return self.object

    def post(self, request, *args, **kwargs):
        logger.warning("Hello from ProjectUpdateView !")
        if "cancel" in request.POST:
            url = self.get_success_url()
            return HttpResponseRedirect(url)
        else:
            return super(ProjectUpdateView, self).post(request, *args, **kwargs)


class ProjectAutocompleteView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        qs = Project.objects.all()

        if self.q:
            qs = qs.filter(title__istartswith=self.q)

        return qs



class ApiEACGetchampionsView(FormView):
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



class ApiEACGetProjectsView(FormView):
    """
    Documentation
    =============

    - https://ccbv.co.uk/projects/Django/1.10/django.views.generic.edit/FormView/

    """
    def get(self, request, *args, **kwargs):
        """term is sent by the jquery-ui autocomplete widget.

        For the jquery-ui autocomplete widget we have to return 3 fields:

        - id
        - label
        - value

        For the jquery EasyAutocomplete we can return what we want.


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
            project_json['label'] = project.title
            project_json['value'] = project.title
            results.append(project_json)

        data = json.dumps(results)
        mimetype = 'application/json'
        return HttpResponse(data, mimetype)
