# Docker Silverstipe

made using docker compose

## how to run 
```docker-compose up -d```

### for new projects
ssh onto the silverstripe docker container
```docker-compose exec web /bin/bash```

and install silverstripe
```composer create-project silverstripe/installer ./ss_site ^4```

## To Do
- [ ] Work out how to keep mysql database state for content reasons
- [ ] Work out how to connect RDS running mysql as database instead
	- [ ] Which means having vars for db names that corrolate with the specific project/site you're on now
- [ ] Work out how to get EFS to work so that all containers are exactly the same they just reference a project folder inside the project Dir
	- [ ] This means you need to figure out how to do more vars in the docker-compose.yml
- [ ] Create makefile for docker build and deploy