from ..errors import *
from ..utils import send_json, pop_args
from ..models import User
from django.views import View


class RegisterView(View):
    def get(self, request):
        keys = ['username', 'email', 'password']
        dic = pop_args(request.POST, *keys)
        filtered = User.objects.filter(username=dic['username'])
        if filtered.count() != 0:
            data = userAlreadyRegistered
        else:
            User.objects.create_user(*dic.values())
            data = registerSucceed
        return send_json(data)
