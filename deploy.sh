#!/bin/bash
. /home/ubuntu/.bashrc
export COMPOSE_PROJECT_NAME=DjangoCrudBoard
REPOSITORY=/home/ubuntu/app/
sudo chown $(whoami) $REPOSITORY
cd $REPOSITORY
sudo chmod +x ./deploy-core.sh
bash ./deploy-core.sh
