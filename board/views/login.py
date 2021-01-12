from django.views import View
from ..responses import *
from ..utils import decode_jwt, send_json, encode_jwt
from django.contrib.auth import authenticate

class LoginView(View):
    def post(self, request):
        session = request.session
        if 'JWT_TOKEN' in session:
            prev_dic = decode_jwt(session)
        else:
            prev_dic = {}
        if 'userid' in prev_dic:
            return send_json(userAlreadyLogin)
        if 'username' not in request.POST or 'password' not in request.POST:
            return send_json(illegalArgument)
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return send_json(userDoesNotMatch)
        encoded = encode_jwt({**prev_dic, 'userid': user.id})
        session['JWT_TOKEN'] = encoded
        data = userLogin
        return send_json(data)

    def get(self, request):
        session = request.session
        if 'JWT_TOKEN' in session:
            prev_dic = decode_jwt(session)
        else:
            prev_dic = {}
        if 'userid' in prev_dic:
            data = userAlreadyLogin
        else:
            data = loginRequired
        return send_json(data)
