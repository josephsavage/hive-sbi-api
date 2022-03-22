import logging
import requests

from datetime import datetime
from datetime import timedelta

from celery import current_app
from celery.schedules import crontab
from django_celery_results.models import TaskResult


logger = logging.getLogger('sbi')

app = current_app._get_current_object()


@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(minute='*/1'),
        sync_members.s(),
        name='sync members',
    )

    sender.add_periodic_task(
        crontab(hour=1, minute=30, day_of_week=1),
        clean_task_results.s(),
        name='clean_task_results',
    )

@app.task(bind=True)
def sync_members(self):
    logger.debug("Sync Members ##############################################")

    return "Good Work"


@app.task
def clean_task_results():
    task_results_to_delete = TaskResult.objects.filter(
        date_done__lt=datetime.now() - timedelta(days=7)
    )

    task_results_count = task_results_to_delete.count()
    task_results_to_delete.delete()

    return "Deleted {} task results".format(task_results_count)
