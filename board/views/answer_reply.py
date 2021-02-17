from ..responses import *
from ..utils import get_user, send_json, pop_args, byte_to_dict
from ..models import Post, User, Reply, AnswerReply
from ..decorators import login_required
from ..utils import decode_jwt
from django.views import View
from django.core.serializers import serialize
from urllib import parse
import json

# 대댓글 TODO


class AnswerReplyView(View):
    def get(self, request):
        if "pk" not in request.GET:  # post.py의 primary key를 받지 못하면 replyRequired 응답
            return send_json(replyRequired)
        data = getSucceedFunc('answer_reply')

        try:
            reply = Reply.objects.get(
                pk=request.GET['pk'])
        except Reply.DoesNotExist:           # Reply 필드 데이터 없으면
            return send_json(replyDoesNotExists)
        answerReplies = json.loads(
            serialize(
                "json",
                AnswerReply.objects.filter(reply=reply)
                .order_by('unique_number')  # 대댓글 오름차순
            )
        )

        for answerReply in answerReplies:
            author_pk = answerReply['fields']['author']
            author = User.objects.filter(pk=author_pk)
            answerReply['fields']['author'] = get_user(author)['data']

        data['data'] = answerReplies
        return send_json(data)

    @login_required  # 로그인 된 사람만 댓글을 쓸 수 있음
    def post(self, request):
        dic = pop_args(request.POST, "pk", "content")
        # 하나라도 없다면 illegalArgument 처리
        if None in dic.values():
            return send_json(illegalArgument)
        session = request.session      # 접속 유저중 특정 유저를 인식
        decoded = decode_jwt(session)  # 암호화 해독
        userid = decoded['userid']
        reply = Reply.objects.filter(pk=dic['pk'])
        if len(reply) == 0:
            return send_json(replyDoesNotExists)
        reply = reply[0]
        author = User.objects.filter(id=userid)
        if len(author) == 0:
            return send_json(AnsDoesNotMatch)
        author = author[0]
        unique_number = len(AnswerReply.objects.filter(reply=reply)) + 1
        AnswerReply.objects.create(reply=reply, author=author,
                                   content=dic['content'], unique_number=unique_number)
        data = answerReplySucceed
        return send_json(data)

    @login_required
    def delete(self, request):
        if 'pk' not in byte_to_dict(request.body):
            return send_json(illegalArgument)
        else:
            user_pk = byte_to_dict(request.body)  # 대댓글 pk
            answer = AnswerReply.objects.get(pk=user_pk['pk'])
        session = request.session      # 접속 유저중 특정 유저를 인식
        decoded = decode_jwt(session)
        userid = decoded['userid']  # 로그인한 유저의 pk

        if userid == answer.author.id:  # 로그인한 유저와 삭제할 대댓글 작성 유저가 같으면
            answer.delete()
            return send_json(deleteAnsreplySucceed)
        else:
            return send_json(AnsDoesNotMatch)
    
    @login_required
    def put(self, request):
        dic = byte_to_dict(request.body)
        if dic.get('pk') is None or dic.get('content') is None:
            return send_json(illegalArgument)
        else:
            filtered = AnswerReply.objects.filter(pk=dic['pk'])
        if len(filtered) != 1:
            return send_json(answerReplyDoesNotExists)
        session = request.session      # 접속 유저중 특정 유저를 인식
        decoded = decode_jwt(session)
        userid = decoded['userid']  # 로그인한 유저의 pk

        if userid == filtered[0].author.id:  # 로그인한 유저와 삭제할 대댓글 작성 유저가 같으면
            filtered.update(content=dic['content'])
            return send_json(changeAnswerReplySucceed)
        else:
            return send_json(AnsDoesNotMatch)