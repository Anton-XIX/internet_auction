from celery import shared_task
from auction.models import Auction
from django.db.models import F
'''Put it in other file'''


def get_or_none(classmodel, **kwargs):
    try:
        return classmodel.objects.get(**kwargs)
    except classmodel.MultipleObjectsReturned as e:
        print('ERR====>', e)

    except classmodel.DoesNotExist:
        return None


@shared_task
def price_changer(auction_id, bid_step):
    auction = Auction.objects.filter(pk=auction_id, lot__is_active=True)
    if auction:
        auction.update(current_price=F('current_price') + bid_step)
        price_changer.apply_async(args=[auction_id, bid_step], countdown=10)

        # auction.current_price += 10
        # auction.save(update_fields=['current_price'])
        # res = AsyncResult(price_changer.id)


'''TODO: add bid value field'''
