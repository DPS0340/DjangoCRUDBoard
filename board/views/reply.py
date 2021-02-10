from ..responses import *
from ..utils import send_json, pop_args
from ..models import AnswerReply, User, Post, Reply
from ..decorators import login_required
from ..utils import decode_jwt
from django.views import View
from django.core.serializers import serialize
import json


# 댓글 TODO

# post title -> ID 변경 TODO

class ReplyView(View):
    def get(self, request):
        if "pk" not in request.GET:
            return send_json(postRequired)
        data = getSucceedFunc('reply')
        try:
            post = Post.objects.get(pk=request.GET["pk"])
        except Post.DoesNotExist:
            return send_json(postDoesNotExists)

        replys = json.loads(
            serialize(
                "json",
                Reply.objects.filter(post=post)
                .order_by('-id')  # 댓글은 오름차순
            )
        )

        for reply in replys:
            pk = reply['pk']
            replies = AnswerReply.objects.filter(reply=pk)
            answer_reply_length = len(replies)
            reply['answer_reply_length'] = answer_reply_length
        
        data['data'] = replys
        return send_json(data)

    @login_required  # 로그인 된 사람만 댓글을 쓸 수 있음
    def post(self, request):
        dic = pop_args(request.POST, "pk", "content")
        # 하나라도 없다면 illegalArgument 처리
        if None in dic.values():
            return send_json(illegalArgument)
        session = request.session
        decoded = decode_jwt(session)
        userid = decoded['userid']
        post = Post.objects.filter(pk=dic['pk'])
        if len(post) == 0:
            return send_json(postDoesNotExists)
        post = post[0]
        author = User.objects.filter(id=userid)
        if len(author) == 0:
            return send_json(AnsDoesNotMatch)
        author = author[0]
        Reply.objects.create(post=post, author=author, content=dic['content'])
        data = replySucceed
        return send_json(data)
