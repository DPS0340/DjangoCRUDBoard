#!/bin/sh

REPOSITORY=/home/ec2-user/app

cd $REPOSITORY

nohup docker-compose down && docker-compose up --build > $REPOSITORY/nohup.out 2>&1 &