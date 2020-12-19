from ..errors import *
from ..utils import sendJson
from ..models import User
from django.views import View

class RegisterView(View):
    def get(self, request):
        keys = ['username', 'email', 'password']
        values = [request.POST[key] for key in keys]
        filtered = User.objects.filter(username=values[0])
        if filtered.count() != 0:
            data = userAlreadyRegistered
        else:
            User.objects.create_user(*values)
            data = registerSucceed
        return sendJson(data)
