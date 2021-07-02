from celery import shared_task
import time
from django.apps import apps


def _model(model_name):
    return apps.get_model('lot', model_name)

'''TODO:
    Optimize queries
    Define bid step
    Convert timedelta (duration field) to seconds 

'''
@shared_task
def price_changer(lot_id, is_active):

    lot = _model('Lot').objects.get(pk=lot_id)
    if lot.is_active:
        lot.auction.current_price += 10
        lot.auction.save()
        time.sleep(4)
        price_changer(lot_id,is_active)
