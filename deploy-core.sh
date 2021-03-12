#!/usr/bin/bash
REPOSITORY=$(dirname `which $0`)
cd $REPOSITORY
echo $Django_secret_key

sudo apt-get update \
  && sudo DEBIAN_FRONTEND=noninteractive apt-get install -y docker-compose

chmod +x ./init-letsencrypt.sh

./init-letsencrypt.sh -n

mkdir -p ./data/db
chmod -R 777 ./data
touch ./nohup.out
docker-compose down -v
nohup docker-compose up --build > ./nohup.out 2>&1 &
