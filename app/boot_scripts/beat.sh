#!/bin/sh
exec su -m app -c 'celery -A hive_sbi_api beat -l info -s /home/app/celerybeat-schedule --pidfile=/home/app/celery.pid'
