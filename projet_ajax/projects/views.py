

import logging

from django.core.urlresolvers import reverse

from django.views.generic.edit import UpdateView
from django.http import HttpResponseRedirect

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


class ProjectUpdateViewEasyAutoComplete(UpdateView):
    """Update thye view with the jQuery EasyAutocomplete plugin.

    Documentation:

    - http://ccbv.co.uk/projects/Django/1.10/django.views.generic.edit/UpdateView/

    """
    model = Project
    form_class = ProjectChampionForm
    context_object_name = 'project'
    template_name = 'projects/project/update_easyautocomplete.html'

    def get_object(self, queryset=None):
        """Pour mémoriser self.demande_article"""
        self.object = super(ProjectUpdateViewEasyAutoComplete, self).get_object(queryset)
        return self.object

    def post(self, request, *args, **kwargs):
        logger.warning("Hello from ProjectUpdateViewEasyAutoComplete !")
        if "cancel" in request.POST:
            url = reverse('projects:project_update_easy', kwargs={'pk': self.pk})
            return HttpResponseRedirect(url)
        else:
            return super(ProjectUpdateViewEasyAutoComplete, self).post(request, *args, **kwargs)



