from django.shortcuts import render

from django.http import HttpResponse
from django.contrib.auth.models import User
import json


def champion_auto_complete(request):
    q = request.REQUEST('term')
    users = User.objects.filter(is_active=True)
    users_list = []

    for u in users:
        value = '{}, {} ({}) - {}'.format(u.last_name,
                                          u.first_name,
                                          u.username,
                                          u.email)
        u_dict = {'id': u.id, 'label': value, 'value': value}
        users_list.append[u_dict]

    return HttpResponse(json.dumps(users_list), mimetype='application/json')

