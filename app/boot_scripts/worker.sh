#!/bin/sh

chown -R app:app /app
chown -R app:app /home/app

exec celery -A hive_sbi_api worker -c 1 -l info
