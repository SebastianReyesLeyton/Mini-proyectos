FROM node:12.13.0
MAINTAINER Juan Sebastian Reyes Leyton <sebas.reyes2002@hotmail.com>

COPY /cloud/. /opt/www
WORKDIR /opt/www

RUN apt-get update && apt-get install nano curl -y
RUN npm install
RUN npm install -g @angular/cli@10.0.3

EXPOSE 4200