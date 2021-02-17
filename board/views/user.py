from ..responses import *
from ..utils import send_json, pop_args, byte_to_dict, get_user
from django.contrib.auth.models import User as Default_User
from ..models import User
from django.contrib.auth.hashers import make_password
from django.views import View
import sys
sys.path.append("../../")
import json
from django.core.serializers import serialize
from DjangoCRUDBoard import settings

class UserView(View):
    def get(self, request):
        keys = ['username']
        dic = pop_args(request.GET, *keys)
        if None in dic.values():
            return send_json(illegalArgument)
        users = User.objects.filter(username=dic['username'])
        result = get_user(users)
        return send_json(result)

    def post(self, request):
        keys = ['username', 'email', 'password']
        dic = pop_args(request.POST, *keys)
        if None in dic.values():
            return send_json(illegalArgument)
        filtered = User.objects.filter(username=dic['username'])
        if filtered.count() != 0:
            return send_json(userAlreadyRegistered)
        User.objects.create_user(*dic.values())
        return send_json(registerSucceed)

    def delete(self, request):
        keys = ['username', 'email', 'password']
        request_dict = byte_to_dict(request.body)
        dic = pop_args(request_dict, *keys)
        if None in dic.values():
            return send_json(illegalArgument)
        filtered = User.objects.filter(username=dic['username'], email=dic['email'])
        if filtered.count() == 0:
            return send_json(noUser)
        if not filtered[0].check_password(dic['password']):
            return send_json(userDoesNotMatch)
        filtered.delete()
        return send_json(deleteUserSucceed)

    def put(self, request):
        keys = ['username', 'email', 'password', 'm_username', 'm_email', 'm_password']
        request_dict = byte_to_dict(request.body)
        dic = pop_args(request_dict, *keys)
        if None in list(dic.values())[:3]: # username, email, password 파라미터 없이 온다면
            return send_json(illegalArgument)
        if not any(list(dic.values())[3:]): # m_username, m_email, m_password 다 아무것도 없을시
            return send_json(illegalModifyArgument)
        filtered = User.objects.filter(username=dic['username'], email=dic['email'])
        if filtered.count() == 0:
            return send_json(noUser)
        if not filtered[0].check_password(dic['password']):
            return send_json(userDoesNotMatch)
        # 변경하려는 username이 기존에 존재하는지 처리 분기문
        filtered_exist = User.objects.filter(username=dic['m_username'])
        if filtered_exist.count() != 0:
            return send_json(userAlreadyRegistered)
        # 변경하려는 아이디, 이메일, 패스워드가 기존과 같다면 어떻게 처리해줘야할지..
        update_value = dic.copy()
        del update_value['m_username'], update_value['m_email'], update_value['m_password']
        '''
        해당 딕셔너리 copy 해준 후 뒷 부분 없애줌. 각 if문 마다 filtered.update해주기에는 비효율적이어서 
        이와 같이 기존 값을 그대로 가지고 있게 하여 m_username만 있고 m_email, m_password없는 등 부분적으로
        컬럼이 없을시에도 기존 값을 가지고 있음으로써 1번만 update해주면 됨
        '''
        if dic['m_username']: 
            update_value['username'] = dic['m_username']
        if dic['m_email']:
            update_value['email'] = dic['m_email']
        if dic['m_password']:
            update_value['password'] = dic['m_password']

        filtered.update(username=update_value['username'], email=update_value['email'], password=make_password(update_value['password']))
        # 현재 이방식은 normalize_email, normalize_username 를 안해주는데 괜찮을지?! create_user 함수 확인 요구됨. 
        return send_json(modifyUserSucceed)
