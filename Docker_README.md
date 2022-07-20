# pull latest version of redis
docker pull redis:latest

# pull specific version of postgres
docker pull postgres:10.10

# pull (if doesn't exist) and run with run
docker run postgres:latest 

# run in background with '-d' 
docker run -d postgres:latest 

# show running containers
docker ps 

# show both running & stopped containers
docker ps -a

# delete a container using container ID from 'docker ps -a'
docker rm <container_ID_HASH>

# show all images downloaded so far
docker images

# delete an image
docker image rm <image_ID> 
# or 
docker image rm <imageName:TAG> # ex: docker image postgres:10.10

# enter into docker command prompt bash interactive-terminal
docker exec -it <container_ID_HASH> /bin/bash

# list all docker network
docker network ls

# create a docker network
docker network create <custom_network_name>

# create and start containers using docker-compose (-d for logs in background)
docker-compose -f mongo.yaml up -d

# start mongo db
docker run -d \
-p 27017:27017 \
-e MONGO_INITDB_ROOT_USERNAME=admin \
-e MONGO_INITDB_ROOT_PASSWORD=password \
--name mongodb \
--net mongo-network \
mongo

# start mongo-express UI
docker run -d \
-p 8081:8081 \
-e ME_CONFIG_MONGODB_ADMINUSERNAME=admin \
-e ME_CONFIG_MONGODB_ADMINPASSWORD=password \
-e ME_CONFIG_MONGODB_SERVER=mongodb \
--net mongo-network \
--name mongo-ui \
mongo-express

# build an image with custom name & version[no version makes it latest] (last parameter is current dir where Dockerfile is present)
docker build -t custom_app_name:1.0  .
