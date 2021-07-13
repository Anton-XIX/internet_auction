import datetime
from celery import shared_task
from auction.models import Auction
from django.db.models import F
from celery import group
from auction.variables import DEACTIVATION_PERIOD


@shared_task
def price_changer(auction_id, bid_step, update_frequency):
    auction = Auction.objects.filter(pk=auction_id, is_active=True).only('pk', 'current_price', 'is_active')
    if auction:
        auction.update(current_price=F('current_price') + bid_step)
        price_changer.apply_async(args=[auction_id, bid_step, update_frequency], countdown=update_frequency)


@shared_task(ignore_result=True)
def deactivate(auction_id):
    auction = Auction.objects.filter(pk=auction_id)
    auction.update(is_active=False)


@shared_task(ignore_result=True)
def deactivate_auctions():
    """
    This task filter auctions that will be expired in next 5 seconds (would be replaced by variable).
    Then it creates group of tasks containing tasks for each auction with eta=end_date
    """
    auctions = Auction.objects.filter(is_active=True, end_date__lte=datetime.datetime.now() + DEACTIVATION_PERIOD).only(
        'pk', 'end_date',
        'is_active')

    if auctions:
        group_tasks = group([deactivate.apply_async(args=[auction.pk], eta=auction.end_date) for auction in auctions])
