from django.db import models
from django.db.models import Q
from .variables import AuctionType


class Auction(models.Model):
    type = models.CharField(max_length=20, choices=AuctionType.choices)
    start_price = models.DecimalField(max_digits=8, decimal_places=2)
    reserve_price = models.DecimalField(max_digits=8, decimal_places=2)
    duration = models.DurationField()
    current_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    update_frequency = models.DurationField(blank=True, null=True)
    buy_now_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f'{self.type} - {self.pk}'

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=(Q(type=AuctionType.English) & Q(buy_now_price__isnull=False) & Q(update_frequency__isnull=True)) |
                      (Q(type=AuctionType.Dutch) & Q(update_frequency__isnull=False) & Q(buy_now_price__isnull=True)),
                name='auction_fields_check'
            ),

        ]
