# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.forms.models import ModelForm
from ajax_select import make_ajax_field
from dal import autocomplete

from .models import (Release,
                     Song,
                     Author,
                     Book)

class ReleaseForm(ModelForm):

    class Meta:
        model = Release
        exclude = []

    # args:  this model, fieldname on this model, lookup_channel_name
    group = make_ajax_field(Release, 'group', 'group', show_help_text=True)

    label = make_ajax_field(Release, 'label', 'label', help_text="Search for label by name")

    # any extra kwargs are passed onto the field, so you may pass a custom help_text here
    # songs = make_ajax_field(Release,'songs','song', help_text=u"Search for song by title")

    # testing bug with no help text supplied
    songs = make_ajax_field(Release, 'songs', 'song', help_text="", show_help_text=True)

    # these are from a fixed array defined in lookups.py
    title = make_ajax_field(Release, 'title', 'cliche', help_text="Autocomplete will suggest clichés about cats.")


class SongForm(ModelForm):
    """The Django form"""

    class Meta:
        model = Song
        fields = ['title', 'group']

    # args:  this model, fieldname on this model, lookup_channel_name
    group = make_ajax_field(Song, # this model
                            'group', # fieldname on this model
                            'group', # lookup_channel_name
                            help_text="Select the group")


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ('name',)
        widgets = {
            'name': autocomplete.Select(url='singers:author_autocomplete')
        }

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author',)
        widgets = {
            'author': autocomplete.ModelSelect2(url='singers:author_autocomplete')
        }


