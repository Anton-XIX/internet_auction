from rest_framework import serializers
from .models import EnglishAuction, DutchAuction


class EnglishAuctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnglishAuction
        fields = '__all__'


class DutchAuctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DutchAuction
        fields = '__all__'
