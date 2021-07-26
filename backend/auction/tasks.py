import datetime
from celery import shared_task
from auction.models import Auction
from django.db.models import F
from celery import group
from auction.variables import DEACTIVATION_PERIOD
from django.core.mail import send_mail
from internet_auction.settings import EMAIL_HOST_USER
from offer.utils import send_updates


@shared_task
def price_changer(auction_id, bid_step, update_frequency):
    auction = Auction.objects.filter(pk=auction_id, deactivate=False).only('pk',
                                                                           'current_price',
                                                                           'deactivate',
                                                                           'is_buy_now_available')

    if auction:
        send_updates(auction.first())
        auction.update(current_price=F('current_price') + bid_step, is_buy_now_available=False)
        price_changer.apply_async(args=[auction_id, bid_step, update_frequency], countdown=update_frequency)


@shared_task(ignore_result=True)
def deactivate(auction_id):
    auction = Auction.objects.get(pk=auction_id)
    auction.deactivate = True
    auction.is_buy_now_available = False
    auction.save(update_fields=['deactivate', 'is_buy_now_available'])

    '''This will be moved into other file'''
    '''If add .only after select_related -> 2 queries instead of 1'''
    offer = auction.offer_set.select_related('user').last()
    if offer:
        title = f'Dear {offer.user.email}'
        message = f'You TOOK A LOT!!!'
        # print(EMAIL_HOST_PASSWORD)
        mail_sent = send_mail(title, message, EMAIL_HOST_USER, [offer.user.email, ])
        return mail_sent


@shared_task(ignore_result=True)
def deactivate_auctions():
    """
    This task filter auctions that will be expired in DEACTIVATION_PERIOD value.
    Then it creates group of tasks containing tasks for each auction with eta=end_date
    """
    auctions = Auction.objects.filter(deactivate=False, end_date__lte=datetime.datetime.now() + DEACTIVATION_PERIOD).only(
        'pk', 'end_date',
        'deactivate')

    if auctions:
        group_tasks = group([deactivate.apply_async(args=[auction.pk], eta=auction.end_date) for auction in auctions])
