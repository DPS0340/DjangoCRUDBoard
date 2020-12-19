from django.views import View
from ..errors import *
from ..utils import sendJson
from django.contrib.auth import authenticate


class LoginView(View):
    def post(self, request):
        if 'userid' in request.session:
            data = userAlreadyLogin
        else:
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                request.session['userid'] = user.id
                data = userLogin
            else:
                data = userDoesNotMatch
        return sendJson(data)
