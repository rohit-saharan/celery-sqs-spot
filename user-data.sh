#!/bin/bash
export AWS_ACCESS_KEY_ID=""
export AWS_SECRET_ACCESS_KEY=""
export AWS_REGION=""
export SQS_URL=""
apt-get update -qq
apt-get -qq -y install python3 python3-pip git
curl -fsSL https://get.docker.com | bash -
curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
cd /opt
git clone https://github.com/geekrohit/celery-sqs-spot.git celery
cd celery
docker-compose up -d
