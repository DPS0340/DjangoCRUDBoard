#!/bin/sh

# https://github.com/aws/aws-codedeploy-agent/issues/14 이슈 참조
if [ -d /home/ubuntu/app/ ]; then
    if [ -d /home/ubuntu/app-backup ]; then
        rm -rf /home/ubuntu/app-backup
    fi
    sudo docker-compose down -v > $REPOSITORY/nohup.out
    mv /home/ubuntu/app /home/ubuntu/app-backup
fi
mkdir -p /home/ubuntu/app

sudo certbot --nginx -d ec2-3-35-233-97.ap-northeast-2.compute.amazonaws.com