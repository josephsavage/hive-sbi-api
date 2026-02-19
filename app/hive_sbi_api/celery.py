import os
import django
import multiprocessing

from celery import Celery
multiprocessing.set_start_method("fork", force=True)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hive_sbi_api.settings")

# Initialize Django BEFORE creating the Celery app or autodiscovering tasks
django.setup()

app = Celery("hive_sbi_api")

# Load Celery config from Django settings
app.config_from_object("django.conf:settings", namespace="CELERY")

# Autodiscover tasks in installed apps
app.autodiscover_tasks()
