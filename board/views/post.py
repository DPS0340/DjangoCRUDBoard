from ..responses import *
from ..utils import send_json, pop_args
from ..models import User, Post
from django.contrib.auth.decorators import login_required
from django.views import View


class PostView(View):
    def get(self, request):
        if "board" not in request.GET:
            return send_json(boardRequired)
        data = getPost
        posts = Post.objects.filter(board=request.GET["board"]).order_by('-created_at')[:10]
        data['data'] = posts
        return send_json(data)

    def post(self, request):
        dic = pop_args(request.POST, "title", "board")
        Post.objects.create(*dic)
        data = postSucceed
        return send_json(data)
