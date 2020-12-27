from ..responses import *
from ..utils import send_json, pop_args
from ..models import Post, Board
from ..decorators import login_required
from django.views import View
from django.core.serializers import serialize
import json

class PostView(View):
    def get(self, request):
        if "board" not in request.GET:
            return send_json(boardRequired)
        data = getSucceedFunc('post')
        try:
            board = Board.objects.get(name=request.GET["board"])
        except Board.DoesNotExist:
            return send_json(boardDoesNotExists)
        posts = json.loads(serialize("json",
        Post.objects
            .filter(board=board)
            .order_by('-id')[:10]))
        data['data'] = posts
        return send_json(data)

    @login_required
    def post(self, request):
        dic = pop_args(request.POST, "title", "board")
        Post.objects.create(*dic)
        data = postSucceed
        return send_json(data)