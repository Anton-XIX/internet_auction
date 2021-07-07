from celery import shared_task
from auction.models import Auction
from django.db.models import F

'''Put it in other file'''


def get_or_none(classmodel, **kwargs):
    try:
        return classmodel.objects.get(**kwargs)
    except classmodel.MultipleObjectsReturned as e:
        print('Error:', e)

    except classmodel.DoesNotExist:
        return None


'''TODO: add bid value field'''


@shared_task
def price_changer(auction_id, bid_step):
    auction = Auction.objects.filter(pk=auction_id, is_active=True)
    if auction:
        auction.update(current_price=F('current_price') + bid_step)
        price_changer.apply_async(args=[auction_id, bid_step], countdown=10)


@shared_task
def deactivate_auction():
    auction = Auction.objects.filter(is_active=True)
    auction.update(is_active=False)
