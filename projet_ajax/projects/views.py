
import json

from django.contrib.auth.models import User

from django.views.generic.edit import UpdateView
from django.http import (HttpResponseRedirect,
                         HttpResponse)

from django.views.generic import FormView

from .models import Project
from .forms import ProjectForm


class ChampionAutoCompleteView(FormView):
    """
    Documentation
    =============

    - https://ccbv.co.uk/projects/Django/1.9/django.views.generic.edit/FormView/

    """
    def get(self,request,*args,**kwargs):
        data = request.GET
        # term is sent by the jquery-ui autocomplete widget
        username = data.get("term")
        if username:
            users = User.objects.filter(username__icontains= username)
        else:
            users = User.objects.all()

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


class ProjectUpdateView(UpdateView):
    """
            url(r'^projects/project/(?P<pk>\d+)/update/$', ProjctUpdate.as_view(), name='project_update'),

    Documentation:

    - http://ccbv.co.uk/projects/Django/1.9/django.views.generic.edit/UpdateView/

    """
    model = Project
    form_class = ProjectForm
    context_object_name = 'project'
    template_name = 'projects/project/update.html'

    def get_object(self, queryset=None):
        """Pour mémoriser self.demande_article"""
        self.object = super(ProjectUpdateView, self).get_object(queryset)
        return self.object

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            url = self.get_success_url()
            return HttpResponseRedirect(url)
        else:
            return super(ProjectUpdateView, self).post(request, *args, **kwargs)

