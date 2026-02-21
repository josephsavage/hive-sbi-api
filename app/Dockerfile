FROM python:3.9.10

ARG DJANGO_ENV

WORKDIR /app/

# Install proper dependencies for PostgreSQL and MariaDB (Removing MS SQL)
RUN apt-get update && apt-get install -y \
    libpq-dev \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# Add requirements and install first to leverage Docker layer caching
ADD requirements /app/requirements
ADD requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && \
    pip install -r requirements/$DJANGO_ENV.txt

# Add the rest of the application files
ADD hive_sbi_api /app/hive_sbi_api
ADD boot_scripts /app/boot_scripts
ADD manage.py /app/manage.py

RUN chmod +x /app/boot_scripts/*.sh

# Create the unprivileged user
RUN adduser --disabled-password --gecos '' app

ENV HOME=/home/app
ENV DJANGO_SETTINGS_MODULE=hive_sbi_api.settings.$DJANGO_ENV
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
ENV DJANGO_ENV=$DJANGO_ENV

# Switch to the unprivileged user for security
USER app

# Fix the directory typo to correctly target boot_scripts
CMD sh /app/boot_scripts/$DJANGO_ENV.sh
