#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""Project Administration.

"""

from django.contrib import admin

from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """Project administration

    Documentation
    =============

    - https://docs.djangoproject.com/en/dev/ref/contrib/admin/#modeladmin-objects

    """
    list_display = ('title', 'champion')
    search_fields = ('title', 'champion')
    list_filter = ('title', 'champion')