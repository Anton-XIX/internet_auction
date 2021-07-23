from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


def set_message(auction, offer=None):
    message = {
        "type": "message",
        "message": {
            "auction_data": {
                "auction_id": auction.pk,
                "current_price": str(auction.current_price),
                "is_active": auction.is_active,
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
    message = set_message(auction, offer)
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(

        f'auction_current_price_{auction.id}',
        message
        )
