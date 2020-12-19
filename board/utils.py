from django.http import HttpResponse
import json


def send_json(data):
    res = json.dumps(data)
    return HttpResponse(res, content_type='application/json')


def pop_args(dict, *args):
    return {arg: dict[arg] for arg in args}
