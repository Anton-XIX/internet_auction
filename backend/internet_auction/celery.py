import os
from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "internet_auction.settings")

app = Celery("internet_auction")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
