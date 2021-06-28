from rest_framework import serializers
from .models import Auction
from .variables import AuctionType

class AuctionSerializer(serializers.ModelSerializer):

    type = serializers.ChoiceField(choices=AuctionType.choices)

    class Meta:
        model = Auction
        fields = '__all__'
