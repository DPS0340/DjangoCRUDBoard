from ..responses import *
from ..utils import send_json, pop_args
from ..models import User, Reply, AnswerReply
from ..decorators import login_required
from ..utils import decode_jwt
from django.views import View
from django.core.serializers import serialize
import json


# 댓글 TODO

# post title -> ID 변경 TODO

class AnswerReplyView(View):
    def get(self, request):
        if "pk" not in request.GET:
            return send_json(replyRequired)
        data = getSucceedFunc('answer_reply')
        try:
            reply = Reply.objects.get(pk=request.GET["pk"])
        except Reply.DoesNotExist:
            return send_json(replyDoesNotExists)
        replys = json.loads(
            serialize(
                "json",
                AnswerReply.objects.filter(reply=reply)
                .order_by('id') # 대댓글은 오름차순
            )
        )
        data['data'] = replys
        return send_json(data)

    @login_required # 로그인 된 사람만 댓글을 쓸 수 있음
    def post(self, request):
        dic = pop_args(request.POST, "pk", "content")
        # 하나라도 없다면 illegalArgument 처리
        if None in dic.values():
            return send_json(illegalArgument)
        session = request.session
        decoded = decode_jwt(session)
        userid = decoded['userid']
        reply = Reply.objects.filter(pk=dic['pk'])[0] 
        author = User.objects.filter(id=userid)[0]
        AnswerReply.objects.create(reply=reply, author=author, content=dic['content'])
        data = replySucceed
        return send_json(data)
