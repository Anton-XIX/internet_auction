import datetime
from celery import shared_task
from auction.models import Auction
from django.db.models import F
from celery import group


@shared_task
def price_changer(auction_id, bid_step, update_frequency):
    auction = Auction.objects.filter(pk=auction_id, is_active=True).only('pk', 'current_price', 'is_active')
    if auction:
        auction.update(current_price=F('current_price') + bid_step)
        price_changer.apply_async(args=[auction_id, bid_step, update_frequency], countdown=update_frequency)


'''Task deactivate_auctions would be optimized!'''


@shared_task
def deactivate_auctions():
    auctions = Auction.objects.filter(is_active=True, end_date__lte=datetime.datetime.now())
    if auctions:
        for auction in auctions:
            auction.deactivate_auction()
