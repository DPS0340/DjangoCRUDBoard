from ..responses import *
from ..utils import send_json, pop_args
from ..models import Post, Board, User, Reply
from ..decorators import login_required
from ..utils import decode_jwt
from django.views import View
from django.core.serializers import serialize
import json

class PostView(View):
    def get(self, request):
        if "pk" not in request.GET:
            return send_json(boardRequired)
        data = getSucceedFunc('post')
        try:
            board = Board.objects.get(pk=request.GET["pk"])
        except Board.DoesNotExist:
            return send_json(boardDoesNotExists)

        post_num = 10
        if "num" in request.GET:
            post_num = int(request.GET["num"])
            
        post_obj = Post.objects.filter(board=board).order_by('unique_number')[:post_num]
        posts = json.loads(
            serialize(
                "json",
                post_obj
            )
        )
        for post in posts:
            pk = post['pk']
            replies = Reply.objects.filter(post=pk)
            reply_length = len(replies)
            post['reply_length'] = reply_length

        data['data'] = posts
        return send_json(data)

    @login_required
    def post(self, request):
        dic = pop_args(request.POST, "pk", "title", "content")
        # 하나라도 없다면 illegalArgument 처리
        if None in dic.values():
            return send_json(illegalArgument)
        session = request.session
        decoded = decode_jwt(session)
        userid = decoded['userid']
        board = Board.objects.filter(pk=dic['pk'])
        if len(board) == 0:
            return send_json(boardDoesNotExists)
        board = board[0]
        author = User.objects.filter(id=userid)
        if len(author) == 0:
            return send_json(AnsDoesNotMatch)
        author = author[0]
        unique_number = len(Post.objects.filter(board=board)) + 1
        Post.objects.create(title=dic['title'], board=board, author=author,
                            content=dic['content'], unique_number=unique_number)
        data = postSucceed
        return send_json(data)
