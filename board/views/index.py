from ..errors import *
from ..utils import sendJson

from django.views import View


class IndexView(View):
    def get(self, request):
        return sendJson(APIOnly)

    def post(self, request):
        return self.get(request)
