from django.db import models
from item.models import Item
from auction.models import Auction
from django.contrib.auth import get_user_model


class Lot(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    user = models.ForeignKey
    is_active = models.BooleanField(default=True)

    # user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f'{self.item} : {self.auction}'


class Offer(models.Model):
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE)

    offer_price = models.DecimalField(max_digits=8, decimal_places=2)
