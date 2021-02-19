#!/bin/sh

REPOSITORY=/home/ubuntu/app

cd $REPOSITORY

sudo apt-get update \
  && sudo DEBIAN_FRONTEND=noninteractive apt-get install -y docker-compose

sudo chmod -R 777 data

sudo docker-compose down -v > $REPOSITORY/nohup.out
nohup sudo docker-compose up --build >> $REPOSITORY/nohup.out 2>&1 &