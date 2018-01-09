##### Stop all containers
docker stop $(docker ps -a -q)
##### Delete all containers
docker rm $(docker ps -a -q)
##### Delete all images
docker rmi $(docker images -q)


##### Run any command inside a container
docker-compose run <container_name> <command>
##### Example:
docker-compose run web python3 manage.py migrate
