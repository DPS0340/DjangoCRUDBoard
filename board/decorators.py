from .utils import sendJson
from .errors import postOnly, loginRequired, userDoesNotMatch
from django.contrib.auth.models import User


def login_required(view):
    def wrapper(*args, **kwargs):
        request = args[0]
        if 'userid' not in request.session:
            return sendJson(loginRequired)
        userid = request.session['userid']
        try:
            User.objects.get(id=userid)
        except User.DoesNotExist:
            return sendJson(userDoesNotMatch)
        return view(*args, **kwargs)

    return wrapper


def post_only(view):
    def wrapper(*args, **kwargs):
        request = args[0]
        if request.method != 'POST':
            return sendJson(postOnly)
        return view(*args, **kwargs)

    return wrapper
