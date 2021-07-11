import datetime
from celery import shared_task
from auction.models import Auction
from django.db.models import F


@shared_task
def price_changer(auction_id, bid_step, update_frequency):
    auction = Auction.objects.filter(pk=auction_id, is_active=True)
    if auction:
        auction.update(current_price=F('current_price') + bid_step)
        price_changer.apply_async(args=[auction_id, bid_step, update_frequency], countdown=update_frequency)


@shared_task
def deactivate_auction():
    auction = Auction.objects.filter(is_active=True, end_date__lte=datetime.datetime.now())
    if auction:
        auction.update(is_active=False)
