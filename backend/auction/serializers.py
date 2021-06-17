from rest_framework import serializers
from .models import Auction


class AuctionSerializer(serializers.ModelSerializer):
    ENGLISH = 'En'
    DUTCH = 'Nl'
    AUCTION_TYPE = [
        (ENGLISH, 'English'),
        (DUTCH, 'Dutch'),
    ]
    type = serializers.ChoiceField(choices=AUCTION_TYPE)

    class Meta:
        model = Auction
        fields = '__all__'
