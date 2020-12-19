from django.views import View
from ..errors import *
from ..models import User
from ..utils import send_json


class LogoutView(View):
    def get(self, request):
        if 'userid' not in request.session:
            data = userAlreadyLogout
        else:
            try:
                User.objects.get(id=request.session['userid'])
                del request.session['userid']
                data = userLogout
            except User.DoesNotExist:
                data = userDoesNotExist
        return send_json(data)

    def post(self, request):
        return self.get(request)
