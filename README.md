# Django Boilerplate Projects

#### This repository contains 3 boilerplate projects separated out by three branches. The master branch contains everything (docker, django, wagtail, & react)
  - Docker, Django
  - Docker, Django, Wagtail
  - Docker, Django, Wagtail, React

## Steps to run locally
  1. Run `docker-compose up`
  2. Run `docker-compose run web python3 manage.py migrate`

## Steps to deploy on Heroku
  1. Run `heroku create [app_name]`
  2. Run `heroku addons:create heroku-postgresql:hobby-dev`
  3. Run `heroku config:set DJANGO_SETTINGS_MODULE=boilerplate_django.settings.heroku`
  4. Run `heroku container:login`
  5. Run `heroku container:push web`
  6. Run `heroku run python3 manage.py migrate`

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
