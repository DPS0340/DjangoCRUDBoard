#!/bin/sh
export COMPOSE_PROJECT_NAME=DjangoCrudBoard
# https://github.com/aws/aws-codedeploy-agent/issues/14 이슈 참조
if [ -d /home/ubuntu/app/ ]; then
    if [ -f /home/ubuntu/app/docker-compose.yml ]; then
        cd /home/ubuntu/app
        sudo docker-compose down -v
    fi
    if [ -d /home/ubuntu/app-backup ]; then
        sudo rm -rf /home/ubuntu/app-backup
    fi
    cd /
    sudo mv /home/ubuntu/app /home/ubuntu/app-backup
fi
mkdir -p /home/ubuntu/app
