# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django import forms

from django.shortcuts import render_to_response

# https://docs.djangoproject.com/en/dev/ref/templates/api/
from django.template import RequestContext
from ajax_select.fields import AutoCompleteField


class SearchForm(forms.Form):

    q = AutoCompleteField('cliche',
        required=True,
        help_text="Autocomplete will suggest clichés about cats, but you can enter anything you like.",
        label="Favorite Cliché",
        attrs={'size': 100})


def search_form(request):

    dd = {}
    if 'q' in request.GET:
        dd['entered'] = request.GET.get('q')
    initial = {'q': "\"This is an initial value,\" said O'Leary."}
    form = SearchForm(initial=initial)
    dd['form'] = form
    return render_to_response('search_form.html',
                              dd,
                              context=RequestContext(request))
