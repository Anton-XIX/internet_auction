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
    # item = ItemSerializer(read_only=True)
    # auction = AuctionSerializer(read_only=True)
    # auction = serializers.JSONField(write_only=True)
    # item = serializers.JSONField(write_only=True)
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(source='item.title')
    description = serializers.CharField(source='item.description')
    photo = serializers.FileField(source='item.photo')
    type = serializers.CharField(source='auction.type')
    start_price = serializers.CharField(source='auction.start_price')
    reserve_price = serializers.CharField(source='auction.reserve_price')
    duration = serializers.CharField(source='auction.duration')
    current_price = serializers.CharField(source='auction.current_price')
    update_frequency = serializers.CharField(source='auction.update_frequency', required=False)
    buy_now_price = serializers.CharField(source='auction.buy_now_price')

    class Meta:
        model = Lot
        fields = ['id', 'title', 'description', 'photo', 'type', 'start_price', 'reserve_price',
                  'duration', 'current_price', 'update_frequency', 'buy_now_price', 'is_active']

    @transaction.atomic
    def create(self, validated_data):
        item_data = validated_data.pop('item')
        auction_data = validated_data.pop('auction')
        item = Item.objects.create(**item_data)
        auction = Auction.objects.create(**auction_data)
        lot = Lot.objects.create(item=item, auction=auction, is_active=True)
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
