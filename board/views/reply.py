from ..responses import *
from ..utils import send_json
from ..models import User
from django.contrib.auth.decorators import login_required
from django.views import View


class ReplyView(View):
    def get(self, request):
        pass

    def post(self, request):
        pass
