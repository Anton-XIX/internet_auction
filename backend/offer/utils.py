from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.core.mail import send_mail
from internet_auction.settings import EMAIL_HOST_USER
from .variables import OfferType


def set_socket_message(auction, offer=None):
    message = {
        "type": "message",
        "message": {
            "auction_data": {
                "auction_id": auction.pk,
                "current_price": str(auction.current_price),
                "deactivate": auction.deactivate,
                "is_buy_now_available": auction.is_buy_now_available
            }}}

    if offer:
        offer_data = {"offer_data": {
            "id": offer.pk,
            "username": offer.user.username,
            "offer_price": str(offer.offer_price),
            "auction": offer.auction.id,
            "user": offer.user.id,

        }}
        message['message'].update(offer_data)
    return message


def send_updates(auction, offer=None):
    message = set_socket_message(auction, offer)
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(

        f'auction_current_price_{auction.id}',
        message
    )


def set_email_message(auction_id, user_email, offer_type, previous_offer=None):
    email_message = {}
    if offer_type == OfferType.Bid and previous_offer:
        email_message['title'] = f'Dear {previous_offer.user.email}'
        email_message['message'] = f'Your offer was rejected by {user_email}'
        email_message['recipient'] = previous_offer.user.email

    else:
        email_message['title'] = f'Dear {user_email}'
        email_message['message'] = f'Your bought lot!'
        email_message['recipient'] = user_email

    return email_message


def send_email_message(auction_id, user_email, offer_type, previous_offer=None):
    email_message = set_email_message(auction_id, user_email, offer_type, previous_offer)
    send_mail(email_message['title'], email_message['message'], EMAIL_HOST_USER, [email_message['recipient'], ])
