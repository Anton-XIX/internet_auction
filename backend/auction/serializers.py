from rest_framework import serializers
from .models import Auction
from .variables import AuctionType
from django.db import transaction
from .tasks import price_changer


class AuctionSerializer(serializers.ModelSerializer):
    type = serializers.ChoiceField(choices=AuctionType.choices)

    class Meta:
        model = Auction
        fields = '__all__'

    def create(self, validated_data):
        auction = Auction.objects.create(**validated_data)
        if Auction.type == AuctionType.Dutch:
            transaction.on_commit(
                lambda: price_changer.apply_async(args=[auction.id, auction.bid_step, auction.update_frequency],
                                                  countdown=auction.update_frequency))
        return auction

