from django.db import models
from django.contrib.auth.models import User as Default_User
from .constants import MAX_CHARFIELD_LENGTH

class User(Default_User):
    isAdmin = models.BooleanField(default=False)

# 게시판 모델
# 이름만 가진다
# id를 추가하여야 하나?
class Board(models.Model):
    name = models.CharField(max_length=MAX_CHARFIELD_LENGTH)

# 글 모델
# 제목, 글쓴이, 게시판, 내용을 가진다
# 파일 저장이 필요할까?
class Post(models.Model):
    title = models.CharField(max_length=MAX_CHARFIELD_LENGTH)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

# 댓글 모델
# 글, 댓글쓴이, 내용을 가진다
class Reply(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

# 대댓글 모델
# 댓글, 대댓글 쓴이, 내용을 가진다
class AnswerReply(models.Model):
    reply = models.ForeignKey(Reply, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
