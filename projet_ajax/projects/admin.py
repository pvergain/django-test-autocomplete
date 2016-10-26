#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""Project Administration.

"""

from django.contrib import admin

from .models import Project

from .forms_django_autocomplete_light import ProjectFormDjangoAutocomplete

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """Project administration

    Documentation
    =============

    - https://docs.djangoproject.com/en/dev/ref/contrib/admin/#modeladmin-objects

    """
    form = ProjectFormDjangoAutocomplete
    list_display = ('title', 'champion')
    search_fields = ('title', 'champion')
    list_filter = ('title', 'champion')