from ..errors import *
from ..utils import send_json
from ..models import User
from django.views import View


class DeleteUserView(View):
    def post(self, request):
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
        return send_json(data)