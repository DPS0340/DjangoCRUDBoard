from django.views import View
from ..responses import *
from ..models import User
from ..utils import send_json
from ..decorators import login_required


class LogoutView(View):
    @login_required
    def get(self, request):
        if 'userid' not in request.session:
            return send_json(userAlreadyLogout)
        try:
            User.objects.get(id=request.session['userid'])
            del request.session['userid']
            data = userLogout
        except User.DoesNotExist:
            data = userDoesNotExist
        return send_json(data)

    @login_required
    def post(self, request):
        return self.get(request)
