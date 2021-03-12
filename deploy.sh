#!/bin/bash
source /home/ubuntu/.bashrc

export COMPOSE_PROJECT_NAME=DjangoCrudBoard

REPOSITORY=$(dirname `which $0`)

sudo chown $(whoami) $REPOSITORY

echo $REPOSITORY

cd $REPOSITORY

sudo apt-get update \
  && sudo DEBIAN_FRONTEND=noninteractive apt-get install -y docker-compose

chmod +x ./init-letsencrypt.sh

sudo ./init-letsencrypt.sh -n


mkdir -p ./data/db

sudo chmod -R 777 ./data

sudo chown -R ubuntu ./data

touch ./nohup.out

sudo docker-compose down -v
sudo -E nohup docker-compose up --build > ./nohup.out 2>&1 &
