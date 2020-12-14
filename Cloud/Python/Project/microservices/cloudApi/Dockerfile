# A simple Flask app container
FROM python:3
MAINTAINER Juan Sebastian Reyes Leyton <sebas.reyes2002@hotmail.com>

# Place app in container
COPY . /opt/www
WORKDIR /opt/www

# Install dependecies.
RUN apt-get update && apt-get install nano curl -y
RUN pip3 install -r requirements.txt

EXPOSE 5000
