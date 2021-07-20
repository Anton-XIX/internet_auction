from rest_framework import serializers
from .models import Offer
from offer.tasks import send_offer_rejection
from django.db import transaction
from user.models import CustomUser
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'

    def send_updates(self, auction_id, current_price, is_active, is_buy_now_available, offer_id, offer_price, auction,
                     user):
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
                        "offer_price": str(offer_price),
                        "auction": auction,
                        "user": user,

                    }

                },
            }
        )

    @transaction.atomic()
    def create(self, validated_data):
        offer = Offer.objects.create(**validated_data)
        auction = validated_data['auction']
        user = validated_data['user']
        auction.current_price = validated_data['offer_price']
        auction.save(update_fields=['current_price'])
        # if offer was rejected -> real_time_update_price won't be called
        self.send_updates(auction.pk, auction.current_price, auction.is_active, auction.is_buy_now_available, offer.pk,
                          offer.offer_price, offer.auction.pk, offer.user.pk, )
        # auction.real_time_update_price()
        transaction.on_commit(
            lambda: send_offer_rejection.apply_async(args=[user.email, auction.pk]))

        return offer

    def validate(self, data):
        offer_price = data['offer_price']
        if offer_price > data['auction'].current_price:
            return data
        raise serializers.ValidationError({'offer_price': 'Bis is lower or equal  current price'})


'''get data for task from validated data or from created instance???'''
