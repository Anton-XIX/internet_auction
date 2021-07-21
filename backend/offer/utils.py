from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


def send_updates(auction_id, current_price, is_active, is_buy_now_available, offer_id, offer_price, auction,
                 user, username):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(

        f'auction_current_price_{auction_id}',
        {
            "type": "message",
            "message": {
                "auction_data": {
                    "auction_id": auction_id,
                    "current_price": str(current_price),
                    "is_active": is_active,
                    "is-buy_now_available": is_buy_now_available
                },
                "offer_data": {
                    "id": offer_id,
                    "username": username,
                    "offer_price": str(offer_price),
                    "auction": auction,
                    "user": user,

                }

            },
        }
    )