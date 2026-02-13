# hive-sbi-api

Docker compose  V3.7 deployment
===============================

### Network

Create a network with the `bridge` driver:

~~~
$ docker network create --driver bridge sbi-bridge
~~~

### Set environment variables

Generate a new `.env` file from the provided template:

~~~
$ cp env.template .env
~~~

Example of `.env` file:

~~~
LANG=C.UTF-8
LC_ALL=C.UTF-8

SECRET_KEY=Secret

POSTGRES_DB=DB
POSTGRES_USER=USER
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
POSTGRES_PASSWORD=XXXpasswordXXX

SBI_DB_NAME=DB
SBI_DB_USER=USER
SBI_DB_PASSWORD=XXXpasswordXXX
SBI_DB_HOST=host-ip
SBI_DB_PORT=port
~~~

**Change SECRET_KEY for a long and secure string.**

# DEVELOPMENT ENVIRONMENT

### Build app image

~~~
$ PORT_NGINX=5009 PORT_DEBUG=8009 IMAGE_SERVICE=$(basename $PWD) docker-compose --project-directory=$(pwd) -f compose/docker-compose.base.yml -f compose/docker-compose.dev.yml build
~~~

### run service

~~~
$ PORT_NGINX=5009 PORT_DEBUG=8009 IMAGE_SERVICE=$(basename $PWD) docker-compose --project-directory=$(pwd) -f compose/docker-compose.base.yml -f compose/docker-compose.dev.yml up
~~~

Application will be exposed on port http://localhost:8009 and through NGINX on port http://localhost:5009.


# PRODUCTION ENVIRONMENT

### Build app image

~~~
docker build app -t hive_sbi_api:0.1.0 --build-arg DJANGO_ENV=prod
~~~

or

~~~
PORT_NGINX=5009 PORT_DEBUG=8009 IMAGE_SERVICE=$(basename $PWD) docker-compose --project-directory=$(pwd) -f compose/docker-compose.base.yml -f compose/docker-compose.prod.yml build
~~~

### run service

~~~
PORT_NGINX=5009 PORT_DEBUG=8009 IMAGE_SERVICE=$(basename $PWD) docker-compose \
  --project-directory=$(pwd) \
  -f compose/docker-compose.base.yml \
  -f compose/docker-compose.prod.yml \
  down

PORT_NGINX=5009 PORT_DEBUG=8009 IMAGE_SERVICE=$(basename $PWD) docker-compose \
  --project-directory=$(pwd) \
  -f compose/docker-compose.base.yml \
  -f compose/docker-compose.prod.yml \
  up -d

~~~

Application will be exposed through NGINX on port http://localhost:5009.


# SYNCHRONIZATION TASK

It is a background task that runs every 2.4 hours and is in charge of synchronizing the Postgres database with the MariaDB database. This task must be executed with a specific schedule, and to achieve this goal [Celery](https://docs.celeryq.dev/en/stable/index.html) is being used.

To perform this task, three components have been deployed, each one in a Docker container:

**Redis DB**: To host tasks queue.

**Celery Worker**: To run batch jobs in the background.

**Celery Beat**: To keep track of when tasks should be executed. Manages the tasks schedule. 

The synchronization function, named `sync_members`, is defnined in the [tasks.py](app/hive_sbi_api/sbi/tasks.py) file in the `sbi` app.


# API docs

This applications supports the first API version available in https://api.steembasicincome.com. Here it is known as API-V0 (Version 0), and supports one endpoint to get members information with a GET request to https://api.hivesbi.com/users/{member-username}/.

Also included here the new API version, or API-V1, available in https://api.hivesbi.com/v1/. It has a browsable API developed with Django Rest Framework.

Swagger documentation is available in https://api.hivesbi.com/docs/.


- [V0 Documentation](README.V0.md)
- [V1 Documentation](README.V1.md)
