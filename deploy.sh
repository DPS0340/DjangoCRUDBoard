#!/bin/bash
. /home/ubuntu/.bashrc
export COMPOSE_PROJECT_NAME=DjangoCrudBoard
REPOSITORY=$(dirname `which $0`)
sudo chown $(whoami) $REPOSITORY
cd $REPOSITORY
sudo chmod +x ./deploy-core.sh
bash ./deploy-core.sh
