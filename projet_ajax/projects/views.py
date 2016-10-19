
import json

from django.contrib.auth.models import User

from django.views.generic.edit import UpdateView
from django.http import (HttpResponseRedirect,
                         HttpResponse)

from django.db.models import Q

from django.views.generic import FormView

from .models import Project
from .forms import ProjectChampionForm


class ChampionAutoCompleteView(FormView):
    """
    Documentation
    =============

    - https://ccbv.co.uk/projects/Django/1.9/django.views.generic.edit/FormView/

    """
    def get(self, request, *args, **kwargs):
        """term is sent by the jquery-ui autocomplete widget.

        The filter is on the username and the user email.

         Documentation
         =============

         - http://api.jqueryui.com/autocomplete/#option-source

         String: When a string is used, the Autocomplete plugin expects that string to point to a URL resource that
         will return JSON data. It can be on the same host or on a different one (must provide JSONP).

         The Autocomplete plugin does not filter the results, instead a query string is added with a term field, which
         the server-side script should use for filtering the results.
         For example, if the source option is set to "http://example.com" and the user types foo, a GET request would
         be made to http://example.com?term=foo. The data itself can be in the same format as the local data
         described above.

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


class ProjectUpdateView(UpdateView):
    """
            url(r'^projects/project/(?P<pk>\d+)/update/$', ProjctUpdate.as_view(), name='project_update'),

    Documentation:

    - http://ccbv.co.uk/projects/Django/1.10/django.views.generic.edit/UpdateView/

    """
    model = Project
    form_class = ProjectChampionForm
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

