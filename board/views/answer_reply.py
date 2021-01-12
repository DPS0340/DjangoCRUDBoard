from ..responses import *
from ..utils import send_json, pop_args
from ..models import User, Reply, AnswerReply
from ..decorators import login_required
from django.views import View
from django.core.serializers import serialize
import json


# 댓글 TODO

class AnswerReplyView(View):
    def get(self, request):
        if "reply" not in request.GET:
            return send_json(replyRequired)
        data = getSucceedFunc('answer_reply')
        try:
            # reply = Reply.objects.get(title=request.GET["reply"])
        except Reply.DoesNotExist:
            return send_json(replyDoesNotExists)
        answer_replys = json.loads(
            serialize(
                "json",
                AnswerReply.objects.filter(reply=reply)
                # order_by 어떻게 추가해줘야 하는지.
            )
        )
        data['data'] = answer_replys
        return send_json(data)

    @login_required # 로그인 된 사람만 대댓글을 쓸 수 있음
    def post(self, request):
        dic = pop_args(request.POST, "reply", "content")
        # 하나라도 없다면 illegalArgument 처리
        if None in dic.values():
            return send_json(illegalArgument)
        userid = int(request.session['userid'])
        dic['reply'] = Post.objects.filter(title=dic['reply'])[0] # post에서 해당 부분의 역할이 무엇인지
        author = User.objects.filter(id=userid)[0]
        AnswerReply.objects.create(**dic, author=author)
        data = answerReplySucceed
        return send_json(data)