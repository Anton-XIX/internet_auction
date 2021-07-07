from django.db import models
from auction.models import Auction
from django.contrib.auth import get_user_model
from .tasks import send_offer_rejection


class Offer(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    offer_price = models.DecimalField(max_digits=8, decimal_places=2)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.pk} - Bid'

    def save(self, *args, **kwargs):
        if self.offer_price <= self.auction.current_price:
            send_offer_rejection.apply_async(args=[self.user.email])
            raise ValueError("Bid is lower then current price")

        self.auction.current_price = self.offer_price
        self.auction.is_buy_now_available = False
        self.auction.save()
        super().save(*args, **kwargs)
