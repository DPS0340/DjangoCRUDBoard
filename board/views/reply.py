from ..responses import *
from ..utils import send_json, pop_args
from ..models import User, Post, Reply
from ..decorators import login_required
from django.views import View
from django.core.serializers import serialize
import json


# 댓글 TODO

# post title -> ID 변경 TODO

class ReplyView(View):
    def get(self, request):
        if "post" not in request.GET:
            return send_json(postRequired)
        data = getSucceedFunc('reply')
        try:
            post = Post.objects.get(title=request.GET["post"])
        except Post.DoesNotExist:
            return send_json(postDoesNotExists)
        replys = json.loads(
            serialize(
                "json",
                Reply.objects.filter(post=post)
                # order_by 어떻게 추가해줘야 하는지.
            )
        )
        data['data'] = replys
        return send_json(data)

    @login_required # 로그인 된 사람만 댓글을 쓸 수 있음
    def post(self, request):
        dic = pop_args(request.POST, "post", "content")
        # 하나라도 없다면 illegalArgument 처리
        if None in dic.values():
            return send_json(illegalArgument)
        userid = int(request.session['userid'])
        dic['post'] = Post.objects.filter(title=dic['post'])[0] # post에서 해당 부분의 역할이 무엇인지
        author = User.objects.filter(id=userid)[0]
        Reply.objects.create(**dic, author=author)
        data = replySucceed
        return send_json(data)
