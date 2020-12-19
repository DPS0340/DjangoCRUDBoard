from ..responses import *
from ..utils import send_json
from ..models import Board
from ..decorators import login_required
from django.views import View
from django.core.serializers import serialize
import json


class BoardView(View):
    def get(self, request):
        data = getSucceedFunc('board')
        boards = json.loads(serialize("json", Board.objects.all()))
        data['data'] = boards
        return send_json(data)

    @login_required
    def post(self, request):
        if Board.objects.filter(name=request.POST['name']):
            return send_json(postingElementExists)
        Board.objects.create(name=request.POST['name'])
        return send_json(postSucceed)
