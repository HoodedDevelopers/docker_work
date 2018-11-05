# Docker Compose exercise
checkout the lab on dockers website [here]:https://docs.docker.com/compose/gettingstarted/#step-8-experiment-with-some-other-commands

## The docker-compose file
docker-compose.yml is what creates all the containers and describes how they interact together in a networking sense.

Services is what descirbes each container.

### Web container
Web container doesnt define an "image" property, meaning that it would use the Dockerfile in the root to create its image

### Redis
Redis defines and image so there for it pulls that image down and runs that image.

## How to run the containers
```docker-compose up``` runs the services in the terminal that you are in

```docker-compose down``` stops the containers and removes them.

```docker-compose ps``` shows all the docker-compose services currently running

```docker-compose up -d``` runs the services in detached mode (in the background)

```docker-compose stop``` to stop your services once you are finsihed with them

```docker-compose down --volumes``` to also remove the data volume used by the Redis container