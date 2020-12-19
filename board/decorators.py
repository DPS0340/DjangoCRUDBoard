from .utils import send_json
from .responses import loginRequired, userDoesNotMatch
from django.contrib.auth.models import User


def login_required(func):
    def wrapper(self, request, *args, **kwargs):
        if 'userid' not in request.session:
            return send_json(loginRequired)
        userid = request.session['userid']
        try:
            User.objects.get(id=userid)
        except User.DoesNotExist:
            return send_json(userDoesNotMatch)
        return func(self, request, *args, **kwargs)

    return wrapper