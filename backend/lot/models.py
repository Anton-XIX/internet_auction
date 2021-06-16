from django.db import models
from item.models import Item
from auction.models import Auction


class Lot(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)


class Offer(models.Model):
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    offer_price = models.DecimalField(max_digits=8, decimal_places=2)
