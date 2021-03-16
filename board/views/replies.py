from ..responses import *
from ..utils import get_user, send_json, pop_args, byte_to_dict
from ..models import AnswerReply, User, Post, Reply
from ..decorators import login_required
from ..utils import decode_jwt
from django.views import View
from django.core.serializers import serialize
import json


class RepliesView(View):
    def get(self, request):
        if "pk" not in request.GET:
            return send_json(postRequired)
        data = getSucceedFunc('replies')
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
            answer_replies = json.loads(
                serialize(
                    "json",
                    answer_replies
                    .order_by('unique_number')  # 댓글은 오름차순
                )
            )
            for answer_reply in answer_replies:
                author_pk = answer_reply['fields']['author']
                author = User.objects.filter(pk=author_pk)
                author = get_user(author)
                answer_reply['fields']['author'] = author['data']
            reply['recomment_data'] = answer_replies

        data['data'] = replies
        return send_json(data)
