from dal import autocomplete

from django import forms

from .models import TestModel


class TestForm(forms.ModelForm):
    class Meta:
        model = TestModel
        fields = ('name', 'test')
        widgets = {
            'test': autocomplete.TaggitSelect2('select2_taggit')
        }
