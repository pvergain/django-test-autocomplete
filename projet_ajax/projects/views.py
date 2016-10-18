
import json

from django.http import HttpResponse
from django.contrib.auth.models import User

from django.views.generic.edit import UpdateView
from django.http import HttpResponseRedirect

from .models import Project
from .forms import ProjectForm

def champion_auto_complete(request):
    q = request.REQUEST('term')
    users = User.objects.filter(is_active=True)
    users_list = []

    for u in users:
        value = '{}, {} ({}) - {}'.format(u.last_name,
                                          u.first_name,
                                          u.username,
                                          u.email)
        u_dict = {'id': u.id, 'label': value, 'value': value}
        users_list.append[u_dict]

    return HttpResponse(json.dumps(users_list), mimetype='application/json')



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

