from django.views import View
from ..responses import *
from ..utils import send_json
from django.contrib.auth import authenticate


class LoginView(View):
    def post(self, request):
        if 'userid' in request.session:
            return send_json(userAlreadyLogin)
        if 'username' not in request.POST or 'password' not in request.POST:
            return send_json(illegalArgument)
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            request.session['userid'] = user.id
            data = userLogin
        else:
            data = userDoesNotMatch
        return send_json(data)

    def get(self, request):
        if 'userid' in request.session:
            data = userAlreadyLogin
        else:
            data = loginRequired
        return send_json(data)
