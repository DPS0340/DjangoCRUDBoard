FROM python:3.8
ENV PYTHONUNBUFFERED 1

RUN apt-get -y update 

ENV Django_secret_key abcde0s&&$uyc)hf_3rv@!a95nasd22e-dxt^9k^7!f+$jxkk+$k-
ENV BOARD_DEBUG 1

# 유저, 그룹 나중에 수정 TODO
# the user to run as
ENV USER root

# how many worker processes should Gunicorn spawn
ENV NUM_WORKERS 3

# which settings file should Django use
ENV DJANGO_SETTINGS_MODULE DjangoCRUDBoard.settings

# WSGI module name
ENV DJANGO_WSGI_MODULE DjangoCRUDBoard.wsgi

ENV PORT 8000

RUN echo "Starting $NAME as `whoami`"

WORKDIR /code
ADD . /code              

RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install

ENTRYPOINT ["/code/bin/gunicorn_start"]
