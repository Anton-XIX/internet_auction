import datetime
import time
from celery import shared_task
from auction.models import Auction
from django.db.models import F
from .utils import duration_to_seconds


@shared_task
def price_changer(auction_id, bid_step, duration):
    auction = Auction.objects.filter(pk=auction_id, is_active=True)
    if auction:
        auction.update(current_price=F('current_price') + bid_step)
        price_changer.apply_async(args=[auction_id, bid_step, duration], countdown=duration)


'''Duration may be removed from model. Task also works with negative timedelta values. Need to check big timedelta 
values. Also datetime.timedelta(seconds = 30) should be in variables.py file. '''


@shared_task
def deactivate_auction():
    auction = Auction.objects.filter(is_active=True, duration__lte=datetime.timedelta(seconds=30))

    if auction:
        auction.update(is_active=False, duration=F('duration') - datetime.timedelta(seconds=30))
