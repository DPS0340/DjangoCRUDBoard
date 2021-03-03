#!/bin/sh

REPOSITORY=$(dirname `which $0`)

sudo chown $(whoami) $REPOSITORY

cd $REPOSITORY

sudo apt-get update \
  && sudo DEBIAN_FRONTEND=noninteractive apt-get install -y docker-compose

chmod +x ./init-letsencrypt.sh

sudo ./init-letsencrypt.sh -n

mkdir -p $REPOSITORY/data/db

sudo chmod -R 777 $REPOSITORY/data

sudo chown -R ubuntu $REPOSITORY/data


sudo docker-compose down -v > $REPOSITORY/nohup.out
sudo nohup docker-compose up --build >> $REPOSITORY/nohup.out 2>&1 &
