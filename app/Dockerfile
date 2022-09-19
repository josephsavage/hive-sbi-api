FROM python:3.9.10

ARG DJANGO_ENV

ADD hive_sbi_api             /app/hive_sbi_api
ADD boot_scripts             /app/boot_scripts
ADD requirements             /app/requirements
ADD requirements.txt         /app/requirements.txt
ADD manage.py                /app/manage.py

WORKDIR /app/

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql17
RUN apt-get install -y unixodbc-dev

RUN pip install --upgrade pip; \
	pip install -r requirements/$DJANGO_ENV.txt

# Crear usuario sin privilegios
RUN adduser --disabled-password --gecos '' app

ENV HOME /home/app
ENV DJANGO_SETTINGS_MODULE hive_sbi_api.settings.$DJANGO_ENV

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV DJANGO_ENV $DJANGO_ENV

CMD sh /app/scripts/$DJANGO_ENV.sh
