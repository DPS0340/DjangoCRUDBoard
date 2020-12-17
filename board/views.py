from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method != 'POST':
        data = {
            'success': False,
            'status': 400,
            'reason': 'only POST allowed'
        }
    else:
        data = {
            'success': True,
            'status': 200
        }
    res = json.dump(data)
    return HttpResponse(res, mimetype="application/json")