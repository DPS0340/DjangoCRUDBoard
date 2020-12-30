from ..utils import send_json
from ..responses import ok
from django.views import View


class StatusView(View):
    def get(self, request):
        return send_json(ok)
