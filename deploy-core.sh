#!/usr/bin/bash
REPOSITORY=/home/ubuntu/app/
cd $REPOSITORY
echo $Django_secret_key
echo $COMPOSE_PROJECT_NAME

sudo apt-get update \
  && sudo DEBIAN_FRONTEND=noninteractive apt-get install -y docker-compose

sudo chmod +x ./init-letsencrypt.sh

./init-letsencrypt.sh -n

mkdir -p ./data/db
sudo chmod -R 777 ./data
docker-compose down -v
nohup docker-compose up --build > ./nohup.out 2>&1 &
