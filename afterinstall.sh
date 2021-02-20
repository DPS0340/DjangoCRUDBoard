
if [ -d /home/ubuntu/app-backup/ ]; then
    mkdir -p /home/ubuntu/app
    mv /home/ubuntu/app-backup/data /home/ubuntu/app/data
    mv /home/ubuntu/app-backup/nginx/logs /home/ubuntu/app/nginx/logs
fi
