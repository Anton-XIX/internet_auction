from django.db import models
from item.models import Item
from auction.models import Auction


class Lot(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_buy_now_available = models.BooleanField(default=True, null=True,blank=True)
    # user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,null=

    def __str__(self):
        return f'{self.pk} - Lot'


