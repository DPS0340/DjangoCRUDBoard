from django.http import HttpResponse
import json


def sendJson(data):
    res = json.dumps(data)
    return HttpResponse(res, content_type='application/json')
