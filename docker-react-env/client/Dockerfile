FROM node:8.7.0-alpine

# Create app directory and use it as the working directory
RUN mkdir -p /srv/app/app-client
WORKDIR /srv/app/app-client

COPY package.json /srv/app/app-client
# COPY package.lock.json /srv/app/app-client

RUN npm install

COPY . /srv/app/app-client

CMD ['npm', 'start']