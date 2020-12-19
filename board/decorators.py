from .utils import send_json
from .errors import loginRequired, userDoesNotMatch
from django.contrib.auth.models import User


def login_required(view):
    def wrapper(*args, **kwargs):
        request = args[0]
        if 'userid' not in request.session:
            return send_json(loginRequired)
        userid = request.session['userid']
        try:
            User.objects.get(id=userid)
        except User.DoesNotExist:
            return send_json(userDoesNotMatch)
        return view(*args, **kwargs)

    return wrapper