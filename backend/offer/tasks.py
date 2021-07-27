from celery import shared_task
from .models import Offer
from .utils import send_email_message


@shared_task
def send_offer_rejection(auction_id, user_email, offer_type):
    previous_offer = Offer.objects.filter(auction=auction_id).exclude(user__email=user_email).last()

    if previous_offer:
        send_email_message(auction_id, user_email, offer_type, previous_offer)
