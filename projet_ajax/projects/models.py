#!/usr/bin/python
# -*- coding: utf8 -*-
"""The project's models.

"""
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.core.urlresolvers import reverse

# https://docs.djangoproject.com/en/dev/ref/contrib/auth/#user-model
from django.contrib.auth.models import User

@python_2_unicode_compatible
class Project(models.Model):
    """A project with a title and a champion which is the foreign key to the auth user.

    Documentation
    =============

    - http://guiqinqian.blogspot.fr/2012/01/using-jquery-auto-complete-in-django.html

    """
    title = models.CharField(max_length=200)
    champion = models.ForeignKey(User)

    def get_absolute_url(self):
        """
        https://docs.djangoproject.com/en/dev/ref/class-based-views/generic-editing/
        """
        return reverse('project:project_detail',
                       kwargs={'pk': self.pk})