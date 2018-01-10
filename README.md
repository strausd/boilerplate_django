# Django Boilerplate Projects

#### This repository contains 3 boilerplate projects separated out by three branches. The master branch contains everything (docker, django, wagtail, & react)
  - Docker, Django
  - Docker, Django, Wagtail
  - Docker, Django, Wagtail, React

## Steps to deploy on Heroku
  1. Create a Heroku Project
  2. Add the postgres add on
  3. run `heroku container:login`
  4. run `heroku container:push web`

## Random Docker commands

#### Delete all containers and images
    docker stop $(docker ps -a -q)
    docker rm $(docker ps -a -q)
    docker rmi $(docker images -q)
###### What is this doing?
  1. Stop all containers
  2. Delete all containers
  3. Delete all images

#### Run a command inside the docker image
    docker-compose run [container_name] [command]
    # example:
    docker-compose run web python3 manage.py migrate
