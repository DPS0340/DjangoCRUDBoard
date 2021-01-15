from ..responses import *
from ..utils import send_json, pop_args
from ..models import Post, User, Reply, AnswerReply
from ..decorators import login_required
from ..utils import decode_jwt
from django.views import View
from django.core.serializers import serialize
import json

# 대댓글 TODO


class AnswerReplyView(View):
    def get(self, request):
        if "pk" not in request.GET:  # post.py의 primary key를 받지 못하면 replyRequired 응답
            return send_json(replyRequired)
        # answer_reply 테이블을 저장? url받는 건가?
        data = getSucceedFunc('answer_reply')

        try:
            reply = Reply.objects.get(
                pk=request.GET['pk'])  # Reply 테이블의 pk를 받는거?
        except Reply.DoesNotExist:           # Reply 필드 데이터 없으면
            return send_json(replyDoesNotExists)
        answerreplys = json.loads(
            serialize(
                "json",
                AnswerReply.objects.filter(reply=reply)
                .order_by('id')  # 대댓글 오름차순
            )
        )
        data['data'] = answerreplys  # 'data' 키에 들어가는 값의 자료형이 딕션?
        return send_json(data)

    @login_required  # 로그인 된 사람만 댓글을 쓸 수 있음
    def post(self, request):
        dic = pop_args(request.POST, "pk", "content")
        # 하나라도 없다면 illegalArgument 처리
        if None in dic.values():
            return send_json(illegalArgument)
        session = request.session      # 접속 유저중 특정 유저를 인식을 위함?
        decoded = decode_jwt(session)  # 암호화 해독
        userid = decoded['userid']
        reply = Reply.objects.filter(pk=dic['pk'])[0]
        author = User.objects.filter(id=userid)[0]
        AnswerReply.objects.create(reply=reply, author=author,
                                   content=dic['content'])
        data = answerReplySucceed
        return send_json(data)
