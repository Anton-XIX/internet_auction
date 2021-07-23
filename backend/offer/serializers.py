from rest_framework import serializers
from .models import Offer
from offer.tasks import send_offer_rejection
from django.db import transaction
from .utils import send_updates
from user.models import CustomUser


class OfferSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', required=False)

    class Meta:
        model = Offer
        fields = '__all__'

    @transaction.atomic()
    def create(self, validated_data):
        offer = Offer.objects.create(**validated_data)
        auction = validated_data['auction']
        user = validated_data['user']
        auction.current_price = validated_data['offer_price']

        if auction.is_buy_now_available:
            auction.is_buy_now_available = False
            auction.is_active = False

        auction.save(update_fields=['current_price', 'is_buy_now_available', 'is_active'])

        transaction.on_commit(
            lambda: send_offer_rejection.apply_async(args=[user.email, auction.pk]))
        transaction.on_commit(
            lambda: send_updates(auction, offer))

        return offer

    def validate(self, data):
        offer_price = data['offer_price']
        if offer_price > data['auction'].current_price:
            return data
        raise serializers.ValidationError({'offer_price': 'Bis is lower or equal  current price'})
