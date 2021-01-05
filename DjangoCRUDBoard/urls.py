from django.contrib import admin
from django.urls import re_path as path
from board.views.index import IndexView
from board.views.register import RegisterView
from board.views.delete_user import DeleteUserView
from board.views.login import LoginView
from board.views.logout import LogoutView
from board.views.post import PostView
from board.views.board import BoardView
from board.views.reply import ReplyView
from board.views.status import StatusView
import sys

sys.path.append("../board")

urlpatterns = [
    path(r'^/?$', IndexView.as_view()),
    path(r'^admin/?$', admin.site.urls),
    path(r'^register/?$', RegisterView.as_view()),
    path(r'^delete_user/?$', DeleteUserView.as_view()),
    path(r'^login/?$', LoginView.as_view()),
    path(r'^logout/?$', LogoutView.as_view()),
    path(r'^post/?$', PostView.as_view()),
    path(r'^board/?$', BoardView.as_view()),
    path(r'^status/?$', StatusView.as_view()),
    path(r'^reply/?$', ReplyView.as_view()),
]
