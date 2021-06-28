from django.db import models
from item.models import Item
from auction.models import Auction
from django.contrib.auth import get_user_model

from django.db.models.signals import post_save
from django.dispatch import receiver


class Lot(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    # user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,null=True)

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
        super().save(*args, **kwargs)


'''Check extra queries, maybe use other way for updating auction current_price. Put into file signals.py 
    Use pre-save signal instead save or use only save
'''


@receiver(post_save, sender=Offer, dispatch_uid="update_current_price")
def update_stock(sender, instance, **kwargs):
    instance.lot.auction.current_price = instance.offer_price
