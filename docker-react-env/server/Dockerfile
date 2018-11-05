FROM node:8.7.0-alpine

# Create App dir
RUN mkdir -p /srv/app/app-server
WORKDIR /srv/app/app-server

COPY package.json /srv/app/app-server
# COPY package.lock.json /srv/app/app-server

RUN npm install

COPY . /srv/app/app-server

CMD ['npm', 'run', 'dev']