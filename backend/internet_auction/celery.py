import os
from celery import Celery
from auction.variables import DEACTIVATION_PERIOD
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "internet_auction.settings")

app = Celery("internet_auction")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
app.conf.beat_schedule = {
    'deactivating_lots': {
        'task': 'auction.tasks.deactivate_auctions',
        'schedule': DEACTIVATION_PERIOD
    }
}

'''TODO: think about schedule of deactivate_auction task'''
