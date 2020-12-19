from django.db import models
from django.contrib.auth.models import User
from .constants import MAX_CHARFIELD_LENGTH

# Create your models here.
class Board(models.Model):
    name = models.CharField(max_length=MAX_CHARFIELD_LENGTH)

class Post(models.Model):
    title = models.CharField(max_length=MAX_CHARFIELD_LENGTH)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

class Reply(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

class AnswerReply(models.Model):
    reply = models.ForeignKey(Reply, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
