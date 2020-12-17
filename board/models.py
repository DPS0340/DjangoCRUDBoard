from django.db import models
import django.contrib.auth.models as authModels

# Create your models here.

class User(authModels.User):
    pass

class Board(models.Model):
    name = models.CharField()

class Post(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField()
    content = models.TextField()

class Reply(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

class AnswerReply(models.Model):
    reply = models.ForeignKey(Reply, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
