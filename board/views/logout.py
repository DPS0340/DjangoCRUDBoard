from django.views import View
from ..responses import *
from ..models import User
from ..utils import send_json, decode_jwt, delete_jwt_param
from ..decorators import login_required

class LogoutView(View):
    @login_required
    def get(self, request):
        session = request.session
        if 'userid' not in session:
            return send_json(userAlreadyLogout)
        exists = True
        decoded = decode_jwt(session)
        if 'userid' not in decoded:
            return send_json(loginRequired)

        try:
            User.objects.get(id=decoded['userid'])
        except User.DoesNotExist:
            exists = False

        if exists:
            delete_jwt_param(session, 'userid')
            data = userLogout
        else:
            data = userDoesNotExist
        return send_json(data)

    @login_required
    def post(self, request):
        return self.get(request)
