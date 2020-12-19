from ..errors import *
from ..utils import send_json

from django.views import View


class IndexView(View):
    def get(self, request):
        return send_json(APIOnly)

    def post(self, request):
        return self.get(request)
