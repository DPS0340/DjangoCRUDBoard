from ..responses import *
from ..utils import send_json, pop_args
from ..models import User
from django.views import View


class DeleteUserView(View):
    def post(self, request):
        keys = ['username', 'email', 'password']
        dic = pop_args(request.POST, *keys)
        if None in dic.values():
            return send_json(illegalArgument)
        filtered = User.objects.filter(**dic)
        if filtered.count() == 0:
            data = noUser
        else:
            filtered.delete()
            data = deleteUserSucceed
        return send_json(data)
