from celery import shared_task
from django.core.mail import send_mail
from internet_auction.settings import EMAIL_HOST_USER
from .models import Offer

@shared_task
def send_offer_rejection(email,auction):
    previous_offer = Offer.objects.filter(auction=auction).exclude(user__email=email).last()
    if previous_offer:
        title = f'Dear {previous_offer.user.email}'
        message = f'Your offer was rejected by {email}'
        # print(EMAIL_HOST_PASSWORD)
        mail_sent = send_mail(title, message, EMAIL_HOST_USER, [previous_offer.user.email, ])
        return mail_sent
