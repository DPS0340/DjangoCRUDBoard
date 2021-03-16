from ..responses import *
from ..utils import get_user, send_json, pop_args, byte_to_dict
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
        data = getSucceedFunc("post")
        try:
            board = Board.objects.get(pk=request.GET["pk"])
        except Board.DoesNotExist:
            return send_json(boardDoesNotExists)

        start = 0
        end = 10
        if "start" in request.GET:
            start = int(request.GET["start"])
        if "end" in request.GET:
            end = int(request.GET["end"])
        if end < start:
            return send_json(illegalArgument)

        post_obj = Post.objects.filter(board=board).order_by("unique_number")[start:end]
        posts = json.loads(serialize("json", post_obj))
        for post in posts:
            author_pk = post["fields"]["author"]
            author = User.objects.filter(pk=author_pk)
            post["fields"]["author"] = get_user(author)["data"]
            pk = post["pk"]
            replies = Reply.objects.filter(post=pk)
            reply_length = len(replies)
            post["reply_length"] = reply_length

        data["data"] = posts
        return send_json(data)

    @login_required
    def post(self, request):
        dic = pop_args(request.POST, "pk", "title", "content")
        # 하나라도 없다면 illegalArgument 처리
        if None in dic.values():
            return send_json(illegalArgument)
        session = request.session
        decoded = decode_jwt(session)
        userid = decoded["userid"]
        board = Board.objects.filter(pk=dic["pk"])
        if len(board) == 0:
            return send_json(boardDoesNotExists)
        board = board[0]
        author = User.objects.filter(id=userid)
        if len(author) == 0:
            return send_json(AnsDoesNotMatch)
        author = author[0]
        unique_number = len(Post.objects.filter(board=board)) + 1
        Post.objects.create(
            title=dic["title"],
            board=board,
            author=author,
            content=dic["content"],
            unique_number=unique_number,
        )
        data = postSucceed
        return send_json(data)

    @login_required
    def delete(self, request):
        if "pk" not in byte_to_dict(request.body):
            return send_json(illegalArgument)
        else:
            dic = byte_to_dict(request.body)  # 대댓글 pk
            filtered = Post.objects.filter(pk=dic["pk"])
        if len(filtered) != 1:
            return send_json(postDoesNotExists)
        session = request.session  # 접속 유저중 특정 유저를 인식
        decoded = decode_jwt(session)
        userid = decoded["userid"]  # 로그인한 유저의 pk

        if userid == filtered[0].author.id:  # 로그인한 유저와 삭제할 대댓글 작성 유저가 같으면
            filtered.delete()
            return send_json(deletePostSucceed)
        else:
            return send_json(postDoesNotMatch)

    @login_required
    def put(self, request):
        dic = byte_to_dict(request.body)
        if dic.get("pk") is None or not any([dic.get("title"), dic.get("content")]):
            return send_json(illegalArgument)
        else:
            filtered = Post.objects.filter(pk=dic["pk"])
        if len(filtered) != 1:
            return send_json(postDoesNotExists)
        session = request.session  # 접속 유저중 특정 유저를 인식
        decoded = decode_jwt(session)
        userid = decoded["userid"]  # 로그인한 유저의 pk

        if userid == filtered[0].author.id:  # 로그인한 유저와 삭제할 대댓글 작성 유저가 같으면
            filtered.update(
                title=dic.get("title") if dic.get("title") else filtered[0].title,
                content=dic.get("content")
                if dic.get("content")
                else filtered[0].content,
            )
            return send_json(changePostSucceed)
        else:
            return send_json(postDoesNotMatch)
