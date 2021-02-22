
if [ -d /home/ubuntu/app-backup/ ]; then
    mkdir -p /home/ubuntu/app
    if [ -d /home/ubuntu/app-backup/data ]; then
        mkdir -p /home/ubuntu/app/data
        mv /home/ubuntu/app-backup/data/* /home/ubuntu/app/data
    fi
    if [ -d /home/ubuntu/app-backup/logs ]; then
        mkdir -p /home/ubuntu/app/nginx
        mv /home/ubuntu/app-backup/nginx/logs /home/ubuntu/app/nginx/logs
    fi
fi
cp /home/ubuntu/app/nginx/nginx-release.conf /home/ubuntu/app/nginx/nginx-app.conf