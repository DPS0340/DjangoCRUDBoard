#!/bin/sh

REPOSITORY=/home/ubuntu/app

sudo chown ubuntu $REPOSITORY

cd $REPOSITORY

sudo apt-get update \
  && sudo DEBIAN_FRONTEND=noninteractive apt-get install -y docker-compose

sudo chmod -R 777 data

mkdir -p data/db

nohup sudo docker-compose up --build >> $REPOSITORY/nohup.out 2>&1 &