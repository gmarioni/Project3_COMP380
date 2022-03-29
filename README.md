# Project3_COMP380 Database Portion

## Overview

For the project we need a Database, this and process will allow us to run a docker container with MySQL inside of it, expose it to our application and even bootstrap/load backup data as we test.

## Requirements
You will need docker and docker-compose install

## How to
Once you have docker and docker-compose installed

In this root directory, simple run
`docker-compose up -d`
This will run the docker-compose.yml file and put it on a background/daemon thread
To confirm the container is running run
`docker ps`
To stop and remove the containers run
`docker-compose down`

With the container running you can execute into the container to run mysql commands if you like
`docker exec -it <container-name> mysql -uroot -p`

Visual Studio code also has a nice plugin to access the database as well.  Connection info can be found in the corresponding db.py file

## What does this do?

Running the Database in a docker container allows everyone to have a local copy to work with, without the need to host a copy and secure it.

This always gives people a chance to learn Docker,SQL etc....
