

import logging

from django.contrib.auth.models import User

from django.db.models import Q
from django.views.generic.edit import UpdateView

from dal import autocomplete

from .models import Project

from .forms_django_autocomplete_light import ProjectFormDjangoAutocomplete

# Get an instance of a logger
logger = logging.getLogger(__name__)


class ApiUserDjangoAutocompleteLight(autocomplete.Select2QuerySetView):
    """https://django-autocomplete-light.readthedocs.io/en/master/tutorial.html"""
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        users = User.objects.all()
        if self.q:
            users = User.objects.filter(Q(username__icontains=self.q)
                                        | Q(email__icontains=self.q)).order_by('username')

        return users


class ProjectDjangoAutoCompleteUpdateView(UpdateView):
    """Update the view with the jQuery UI Autocomplete plugin.

    Documentation:

    - http://ccbv.co.uk/projects/Django/1.10/django.views.generic.edit/UpdateView/

    """
    model = Project
    form_class = ProjectFormDjangoAutocomplete
    context_object_name = 'project'
    template_name = 'projects/project/update_django_autocomplete_light.html'

    def get_object(self, queryset=None):
        """Pour mémoriser self.demande_article"""
        self.object = super(ProjectDjangoAutoCompleteUpdateView, self).get_object(queryset)
        return self.object

    def post(self, request, *args, **kwargs):
        logger.warning("Hello from ProjectDjangoAutoCompleteUpdateView !")
        return super(ProjectDjangoAutoCompleteUpdateView, self).post(request, *args, **kwargs)





class ProjectAutocompleteView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        qs = Project.objects.all()

        if self.q:
            qs = qs.filter(title__istartswith=self.q)

        return qs

