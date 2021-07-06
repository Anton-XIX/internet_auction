from django.db import models
from auction.models import Auction


class Offer(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    offer_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.pk} - Bid'

    def save(self, *args, **kwargs):
        if self.offer_price <= self.auction.current_price:
            raise ValueError("Bid is lower then current price")

        self.auction_current_price = 5000
        self.auction.save()
        super().save(*args, **kwargs)
