#!/bin/sh

REPOSITORY=/home/ubuntu/app

cd $REPOSITORY

nohup docker-compose down && docker-compose up --build > $REPOSITORY/nohup.out 2>&1 &