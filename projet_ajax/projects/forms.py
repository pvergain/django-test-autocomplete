# -*- coding: utf-8 -*-


from django import forms

from .models import Project

class ProjectChampionForm(forms.ModelForm):
    """The champion project form"""
    champion_display = forms.CharField(max_length=100,
                                       help_text='type username or email')

    class Meta:
        model = Project
        fields = ('title', 'champion_display', 'champion',)

    def __init__(self, *args, **kwargs):
        super(ProjectChampionForm, self).__init__(*args, **kwargs)
        self.fields['champion_display'].label = "Update the Champion"
        self.fields['champion'].widget = forms.HiddenInput()