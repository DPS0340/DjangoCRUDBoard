from ..responses import *
from ..utils import send_json, pop_args
from ..models import User
from django.views import View
from django.contrib.auth.hashers import make_password
from urllib import parse
import sys
sys.path.append("../../")
from DjangoCRUDBoard import settings

def byte_to_dict(data):
    body_unicode = data.decode('utf-8')
    body = body_unicode.replace("&", "=")
    body_list = body.split("=")
    body_key = []
    body_value = []
    for i in range(len(body_list)):
        if i % 2 == 0:
            body_key.append(body_list[i])
        else:
            body_value.append(parse.unquote(body_list[i]))
    dict_body = dict(zip(body_key, body_value))
    return dict_body

class UserView(View):
    def post(self, request):
        keys = ['username', 'email', 'password']
        dic = pop_args(request.POST, *keys)
        if None in dic.values():
            return send_json(illegalArgument)
        filtered = User.objects.filter(username=dic['username'])
        if filtered.count() != 0:
            data = userAlreadyRegistered
        else:
            User.objects.create_user(*dic.values())
            data = registerSucceed
        return send_json(data)

    def delete(self, request):
        keys = ['username', 'email', 'password']
        request_dict = byte_to_dict(request.body)
        dic = pop_args(request_dict, *keys)
        if None in dic.values():
            return send_json(illegalArgument)
        filtered = User.objects.filter(username=dic['username'], email=dic['email'])
        if filtered.count() == 0:
            data = noUser 
        else:
            if filtered[0].check_password(dic['password']):
                filtered.delete()
                data = deleteUserSucceed
            else:
                data = userDoesNotMatch
        return send_json(data)

    # put