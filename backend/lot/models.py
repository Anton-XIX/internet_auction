from django.db import models
from item.models import Item
from auction.models import Auction
from user.models import CustomUser


class Lot(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return f'{self.pk} - Lot'
