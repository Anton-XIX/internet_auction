from rest_framework import serializers
from .models import Lot, Offer
from item.serializers import ItemSerializer
from auction.serializers import AuctionSerializer
from auction.models import Auction
from item.models import Item
from django.db import transaction


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'


class LotNestedSerializer(serializers.ModelSerializer):
    item = ItemSerializer()
    auction = AuctionSerializer()

    class Meta:
        depth = 1
        model = Lot
        fields = '__all__'

    @transaction.atomic
    def create(self, validated_data):
        item_data = validated_data.pop('item')
        auction_data = validated_data.pop('auction')
        item = Item.objects.create(**item_data)
        auction = Auction.objects.create(**auction_data)
        lot = Lot.objects.create(item=item, auction=auction, **validated_data)
        return lot


'''May be removed'''
# class LotRetrieveSerializer(serializers.ModelSerializer):
#     item = ItemSerializer()
#     auction = AuctionSerializer()
#     offer = OfferSerializer(source='offer_set', many=True)
#
#     class Meta:
#
#         model = Lot
#         fields = '__all__'
