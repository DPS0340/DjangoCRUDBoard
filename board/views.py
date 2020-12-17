from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.models import User
import json
# Create your views here.

def sendJson(data):
    res = json.dumps(data)
    return HttpResponse(res, content_type='application/json')

def index(request):
    data = {
        'success': False,
        'status': 404,
        'comment': 'API Only'
    }
    return sendJson(data)
    
def register(request):
    if request.method != 'POST':
        data = {
            'success': False,
            'status': 400,
            'comment': 'only POST allowed'
        }
    else:
        keys = ['username', 'email', 'password']
        values = [request.POST[key] for key in keys]
        filtered = User.objects.filter(username=values[0])
        if filtered.count() != 0:
            data = {
                'success': True,
                'status': 403,
                'comment': 'User already registered'
            } 
        else:
            User.objects.create_user(*values)
            data = {
                'success': True,
                'status': 200,
                'comment': 'register succeed'
            }
    return sendJson(data)

def delete_user(request):
    if request.method != 'POST':
        data = {
            'success': False,
            'status': 400,
            'comment': 'only POST allowed'
        }
    else:
        keys = ['username', 'email', 'password']
        values = [request.POST[key] for key in keys]
        dic = dict()
        for k, v in zip(keys, values):
            dic[k] = v
        filtered = User.objects.filter(**dic)
        if filtered.count() == 0:
            data = {
                'success': True,
                'status': 401,
                'comment': 'there\'s no matched user'
            }  
        else:
            filtered.delete()
            data = {
                'success': True,
                'status': 200,
                'comment': 'delete user succeed'
            }
    return sendJson(data)