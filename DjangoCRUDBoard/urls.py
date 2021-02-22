from board.views.isAdmin import IsAdminView
from board.views.promote import PromoteView
from django.contrib import admin
from django.urls import re_path as path
from django.urls import include
from board.views.index import IndexView
from board.views.user import UserView
from board.views.login import LoginView
from board.views.logout import LogoutView
from board.views.post import PostView
from board.views.board import BoardView
from board.views.reply import ReplyView
from board.views.answer_reply import AnswerReplyView
from board.views.status import StatusView
import sys


sys.path.append("../board")

urlpatterns = [
    path("", include("django_prometheus.urls")),
    path(r"^/?$", IndexView.as_view()),
    path(r"^admin/?$", admin.site.urls),
    path(r"^register/?$", UserView.as_view()),
    path(r"^user/?$", UserView.as_view()),
    path(r"^login/?$", LoginView.as_view()),
    path(r"^logout/?$", LogoutView.as_view()),
    path(r"^post/?$", PostView.as_view()),
    path(r"^board/?$", BoardView.as_view()),
    path(r"^status/?$", StatusView.as_view()),
    path(r"^reply/?$", ReplyView.as_view()),
    path(r"^answer_reply/?$", AnswerReplyView.as_view()),
    path(r"^promote/?$", PromoteView.as_view()),
    path(r"^is_admin/?$", IsAdminView.as_view()),
]
