

import logging

from django.contrib.auth.models import User

from django.db.models import Q
from dal import autocomplete

from .models import Project

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



class ProjectAutocompleteView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        qs = Project.objects.all()

        if self.q:
            qs = qs.filter(title__istartswith=self.q)

        return qs

