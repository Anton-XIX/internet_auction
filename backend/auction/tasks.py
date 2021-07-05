from celery import shared_task
import time
from django.apps import apps
from auction.models import Auction
import celery

'''Put it in other file'''


def get_or_none(classmodel, **kwargs):
    try:
        return classmodel.objects.get(**kwargs)
    except classmodel.MultipleObjectsReturned as e:
        print('ERR====>', e)

    except classmodel.DoesNotExist:
        return None


@shared_task
def price_changer(auction_id):
    auction = get_or_none(Auction, pk=auction_id)
    print(auction_id)
    if auction:
        auction.current_price += 10
        auction.save()

        price_changer.apply_async(args=[auction_id], countdown=10)
        # price_changer(auction_id)


'''Too many calls of task caused by apply_async'''
