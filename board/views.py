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
        User.objects.create_user(*values)
        User.save()
        data = {
            'success': True,
            'status': 200,
            'comment': 'register succeed'
        }
    return sendJson(data)