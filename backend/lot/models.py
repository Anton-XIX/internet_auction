from django.db import models
from item.models import Item
from auction.models import Auction


class Lot(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    # is_active = models.BooleanField(default=True)




    def __str__(self):
        return f'{self.pk} - Lot'


