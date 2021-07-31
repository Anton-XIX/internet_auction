from rest_framework import serializers
from .models import Lot
from auction.models import Auction
from item.models import Item
from django.db import transaction

from rest_framework_simplejwt.models import TokenUser


# token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
# data = {'token': token}
#    try:
#       valid_data = TokenBackend(algorithm='HS256').decode(token,verify=False)
#       user = valid_data['user']
#       request.user = user
#    except ValidationError as v:
#       print("validation error", v)

class LotNestedSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(source='item.title')
    description = serializers.CharField(source='item.description')
    photo = serializers.FileField(source='item.photo', required=False, allow_null=True)
    auction_id = serializers.CharField(source='auction.pk', read_only=True)
    type = serializers.CharField(source='auction.type')
    start_price = serializers.DecimalField(source='auction.start_price', max_digits=8, decimal_places=2)
    reserve_price = serializers.DecimalField(source='auction.reserve_price', max_digits=8, decimal_places=2)
    end_date = serializers.DateTimeField(source='auction.end_date', format="%Y-%m-%d %H:%M:%S")
    current_price = serializers.DecimalField(source='auction.current_price', max_digits=8, decimal_places=2)
    update_frequency = serializers.DurationField(source='auction.update_frequency', required=False)
    bid_step = serializers.DecimalField(source='auction.bid_step', required=False, max_digits=8, decimal_places=2)
    buy_now_price = serializers.DecimalField(source='auction.buy_now_price', max_digits=8, decimal_places=2)
    is_buy_now_available = serializers.BooleanField(source='auction.is_buy_now_available', read_only=True)
    deactivate = serializers.BooleanField(source='auction.deactivate', default=False)

    class Meta:
        model = Lot
        fields = ['id', 'title', 'description', 'photo', 'auction_id', 'type', 'start_price', 'reserve_price',
                  'end_date', 'current_price', 'update_frequency', 'bid_step', 'buy_now_price', 'deactivate',
                  'is_buy_now_available']

    # def save(self, **kwargs):
    #     obj = super(LotNestedSerializer, self).save(**kwargs)
    #     obj.auction.real_time_update_price()
    #     return obj

    @transaction.atomic
    def create(self, validated_data):
        item_data = validated_data.pop('item')
        auction_data = validated_data.pop('auction')
        user = validated_data.pop('user')
        item = Item.objects.create(**item_data)
        auction = Auction.objects.create(**auction_data)

        lot = Lot.objects.create(item=item, auction=auction, user=user)
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
