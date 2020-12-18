from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import json
from .errors import *


# Create your views here.

def sendJson(data):
    res = json.dumps(data)
    return HttpResponse(res, content_type='application/json')


def index(request):
    return sendJson(APIOnly)


def register(request):
    if request.method != 'POST':
        data = postOnly
    else:
        keys = ['username', 'email', 'password']
        values = [request.POST[key] for key in keys]
        filtered = User.objects.filter(username=values[0])
        if filtered.count() != 0:
            data = userAlreadyRegistered
        else:
            User.objects.create_user(*values)
            data = registerSucceed
    return sendJson(data)


def delete_user(request):
    if request.method != 'POST':
        data = postOnly
    else:
        keys = ['username', 'email', 'password']
        values = [request.POST[key] for key in keys]
        dic = dict()
        for k, v in zip(keys, values):
            dic[k] = v
        filtered = User.objects.filter(**dic)
        if filtered.count() == 0:
            data = noUser
        else:
            filtered.delete()
            data = deleteUserSucceed
    return sendJson(data)


def login(request):
    if request.method != 'POST':
        data = postOnly
    elif 'userid' in request.session:
        data = userAlreadyLogin
    else:
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            request.session['userid'] = user.id
            data = userLogin
        else:
            data = userDoesNotMatch
    return sendJson(data)


def logout(request):
    if 'userid' not in request.session:
        data = userAlreadyLogout
    else:
        try:
            User.objects.get(id=request.session['userid'])
            del request.session['userid']
            data = userLogout
        except User.DoesNotExist:
            data = userDoesNotExist
    return sendJson(data)
