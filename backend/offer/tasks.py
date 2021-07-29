from celery import shared_task
from .models import Offer
from .utils import send_email_message


@shared_task
def send_offer_rejection(auction_id, user_email, offer_id, offer_type):
    previous_offer = Offer.objects.filter(auction=auction_id).exclude(id=offer_id).last()

    if previous_offer and (previous_offer.user.email != user_email):
        send_email_message(auction_id, user_email, offer_type, previous_offer)
