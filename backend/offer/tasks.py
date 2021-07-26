from celery import shared_task
from .models import Offer
from .utils import send_email_message


@shared_task
def send_offer_rejection(user, auction, offer_type):
    previous_offer = Offer.objects.filter(auction=auction.id).exclude(user__email=user.email).last()
    if previous_offer:
        send_email_message(auction, user, offer_type, previous_offer)
