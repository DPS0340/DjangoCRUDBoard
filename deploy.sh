#!/bin/bash
source /home/ubuntu/.bashrc

export COMPOSE_PROJECT_NAME=DjangoCrudBoard

REPOSITORY=$(dirname `which $0`)

chown $(whoami) $REPOSITORY

echo $REPOSITORY

cd $REPOSITORY

sudo apt-get update \
  && sudo DEBIAN_FRONTEND=noninteractive apt-get install -y docker-compose

chmod +x ./init-letsencrypt.sh

./init-letsencrypt.sh -n


mkdir -p ./data/db

chmod -R 777 ./data

chown -R ubuntu ./data

touch ./nohup.out

docker-compose down -v
nohup docker-compose up --build > ./nohup.out 2>&1 &
