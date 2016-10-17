# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django import forms

from django.shortcuts import render_to_response

# https://docs.djangoproject.com/en/dev/ref/templates/api/
from django.template import RequestContext
from django.http import HttpResponseRedirect

from django.views.generic.edit import UpdateView

from django.core.urlresolvers import reverse

from ajax_select.fields import AutoCompleteField

from .models import Song

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



class SongUpdate(UpdateView):
    """
            url(r'^singers/song/(?P<pk>\d+)/update/$', SongUpdate.as_view(), name='song_update'),
    """
    model = Song
    context_object_name = 'song'
    template_name = 'singers/song/update.html'

    def get_object(self, queryset=None):
        """Pour mémoriser self.demande_article"""
        self.object = super(SongUpdate, self).get_object(queryset)
        return self.object

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            url = self.get_success_url()
            return HttpResponseRedirect(url)
        else:
            return super(SongUpdate, self).post(request, *args, **kwargs)

    #def get_success_url(self):
    #    return reverse('article:demande_codif_article_articles_update',
    #                   kwargs={'pk': self.demande_article.pk})