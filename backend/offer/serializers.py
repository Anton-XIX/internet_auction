from rest_framework import serializers
from .models import Offer
from offer.tasks import send_offer_rejection
from django.db import transaction
from user.models import CustomUser


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'

    @transaction.atomic()
    def create(self, validated_data):

        offer = Offer.objects.create(**validated_data)
        auction = validated_data['auction']
        user = validated_data['user']
        auction.current_price = validated_data['offer_price']
        auction.save(update_fields=['current_price'])
        # if offer was rejected -> real_time_update_price won't be called
        auction.real_time_update_price()
        transaction.on_commit(
            lambda: send_offer_rejection.apply_async(args=[user.email, auction.pk]))

        return offer

    def validate(self, data):
        offer_price = data['offer_price']
        if offer_price > data['auction'].current_price:
            return data
        raise serializers.ValidationError({'offer_price': 'Bis is lower or equal  current price'})


'''get data for task from validated data or from created instance???'''
