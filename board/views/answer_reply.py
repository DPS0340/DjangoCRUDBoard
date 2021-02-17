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
        
    def put(self, request):
        keys = ['pk',  'content']
        request_dict = byte_to_dict(request.body)
        dic = pop_args(request_dict, *keys)
        if None in list(dic.values())[:1]: # username, email, password 파라미터 없이 온다면
            return send_json(illegalArgument)
        if None in list(dic.values())[1:]: # m_username, m_email, m_password 다 아무것도 없을시
            return send_json(illegalModifyArgument)
        filtered = AnswerReply.objects.filter(pk=dic['pk'])
        if filtered.count() == 0:
            return send_json(answerReplyDoesNotExists)
        if not filtered[0].check_password(dic['password']):
            return send_json(userDoesNotMatch)
        # 변경하려는 username이 기존에 존재하는지 처리 분기문
        filtered_exist = User.objects.filter(username=dic['m_username'])
        if filtered_exist.count() != 0:
            return send_json(userAlreadyRegistered)
        # 변경하려는 아이디, 이메일, 패스워드가 기존과 같다면 어떻게 처리해줘야할지..
        update_value = dic.copy()
        del update_value['m_username'], update_value['m_email'], update_value['m_password']
        '''
        해당 딕셔너리 copy 해준 후 뒷 부분 없애줌. 각 if문 마다 filtered.update해주기에는 비효율적이어서 
        이와 같이 기존 값을 그대로 가지고 있게 하여 m_username만 있고 m_email, m_password없는 등 부분적으로
        컬럼이 없을시에도 기존 값을 가지고 있음으로써 1번만 update해주면 됨
        '''
        if dic['m_username']: 
            update_value['username'] = dic['m_username']
        if dic['m_email']:
            update_value['email'] = dic['m_email']
        if dic['m_password']:
            update_value['password'] = dic['m_password']

        filtered.update(username=update_value['username'], email=update_value['email'], password=make_password(update_value['password']))
        # 현재 이방식은 normalize_email, normalize_username 를 안해주는데 괜찮을지?! create_user 함수 확인 요구됨. 
        return send_json(modifyUserSucceed)