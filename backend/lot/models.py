from django.db import models
from item.models import Item
from auction.models import Auction


class Lot(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    # user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,null=

    def __str__(self):
        return f'{self.pk} - Lot'


class Offer(models.Model):
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE)
    offer_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.pk} - Bid'

    def save(self, *args, **kwargs):
        if self.offer_price < self.lot.auction.current_price:
            raise ValueError("Bid is lower then current price")
        self.lot.auction.current_price = self.offer_price
        self.lot.auction.save()
        super().save(*args, **kwargs)
