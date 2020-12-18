from django.contrib.auth import authenticate
from .errors import *
from .decorators import *
from .utils import sendJson


# Create your views here.



def index(request):
    return sendJson(APIOnly)


@post_only
def register(request):
    keys = ['username', 'email', 'password']
    values = [request.POST[key] for key in keys]
    filtered = User.objects.filter(username=values[0])
    if filtered.count() != 0:
        data = userAlreadyRegistered
    else:
        User.objects.create_user(*values)
        data = registerSucceed
    return sendJson(data)


@post_only
def delete_user(request):
    keys = ['username', 'email', 'password']
    values = [request.POST[key] for key in keys]
    dic = dict()
    for k, v in zip(keys, values):
        dic[k] = v
    filtered = User.objects.filter(**dic)
    if filtered.count() == 0:
        data = noUser
    else:
        filtered.delete()
        data = deleteUserSucceed
    return sendJson(data)


@post_only
def login(request):
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

@login_required
def logout(request):
    if 'userid' not in request.session:
        data = userAlreadyLogout
    else:
        try:
            User.objects.get(id=request.session['userid'])
            del request.session['userid']
            data = userLogout
        except User.DoesNotExist:
            data = userDoesNotExist
    return sendJson(data)

