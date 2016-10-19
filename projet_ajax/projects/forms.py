#!/usr/bin/python
# -*- coding: utf8 -*-
"""The project's forms.

"""

from django import forms

from .models import Project

class ProjectChampionForm(forms.ModelForm):
    """The champion project form"""
    champion_term = forms.CharField(max_length=100,
                                       help_text='type username or email')

    class Meta:
        model = Project
        fields = ('title',
                  'champion_term', 'champion',)

    def __init__(self, *args, **kwargs):
        super(ProjectChampionForm, self).__init__(*args, **kwargs)
        self.fields['champion_term'].label = "Update the champion"
        self.fields['champion'].widget = forms.HiddenInput()