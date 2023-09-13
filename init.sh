#!/bin/bash

# docker-compose up -d

# mysql -h 127.0.0.1 -P 3306 -u $MYSQL_USER -p$MYSQL_PASSWORD $MYSQL_DATABASE

#docker build -t mysql-app .

#docker volume create my-volume

#docker run -p 5000:5000 -v my-volume:/code my-chat-app  -after care in volumes

#docker run -d -p 3306:3306 --name mysql-container mysql-app
docker-compose up --build