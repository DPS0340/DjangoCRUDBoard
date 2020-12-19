from ..errors import *
from ..utils import sendJson
from ..models import User
from django.contrib.auth.decorators import login_required
from django.views import View


class PostView(View):
    def get(self, request):
        pass

    def post(self, request):
        pass
