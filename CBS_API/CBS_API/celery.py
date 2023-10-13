from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CBS_API.settings")

app = Celery("CBS_API")
app.conf.enable_utc = False
app.conf.broker_connection_retry_on_startup = True
app.conf.update(timezone="Africa/Accra")

app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
