from ..responses import *
from ..utils import get_user, send_json, pop_args, byte_to_dict
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

        replies = json.loads(
            serialize(
                "json",
                Reply.objects.filter(post=post)
                .order_by('unique_number')  # 댓글은 오름차순
            )
        )

        for reply in replies:
            author_pk = reply['fields']['author']
            author = User.objects.filter(pk=author_pk)
            reply['fields']['author'] = get_user(author)['data']
            pk = reply['pk']
            answer_replies = AnswerReply.objects.filter(reply=pk)
            answer_reply_length = len(answer_replies)
            reply['answer_reply_length'] = answer_reply_length
        
        data['data'] = replies
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
        unique_number = len(Reply.objects.filter(post=post)) + 1
        Reply.objects.create(post=post, author=author,
                             content=dic['content'], unique_number=unique_number)
        data = replySucceed
        return send_json(data)

    @login_required
    def put(self, request):
        dic = byte_to_dict(request.body)
        if dic.get('pk') is None or dic.get('content') is None:
            return send_json(illegalArgument)
        else:
            filtered = Reply.objects.filter(pk=dic['pk'])
        if len(filtered) != 1:
            return send_json(replyDoesNotExists)
        session = request.session      # 접속 유저중 특정 유저를 인식
        decoded = decode_jwt(session)
        userid = decoded['userid']  # 로그인한 유저의 pk

        if userid == filtered[0].author.id:  # 로그인한 유저와 삭제할 대댓글 작성 유저가 같으면
            filtered.update(content=dic['content'])
            return send_json(changeReplySucceed)
        else:
            return send_json(AnsDoesNotMatch)