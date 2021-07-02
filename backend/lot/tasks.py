from celery import shared_task
from .models import Lot
import time

'''TODO: Create some step for updating_price, convert duration into seconds
'''
@shared_task
def price_changer(lot_id):
    lot = Lot.objects.get(pk=lot_id)
    if lot.is_active:
        lot.auction.current_price += 10
        lot.auction.save()
        time.sleep(4)
        price_changer(lot_id)
