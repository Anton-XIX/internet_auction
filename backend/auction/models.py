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
    bid_step = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    buy_now_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f'{self.type} - {self.pk}'

    def duration_to_seconds(self):
        return self.duration.seconds

    def save(self, *args, **kwargs):
        if not self.current_price:
            self.current_price = self.start_price

        super().save(*args, **kwargs)

        if self.type == AuctionType.Dutch:
            from .tasks import price_changer
            price_changer.apply_async(args=[self.pk, self.bid_step], countdown=self.duration_to_seconds())

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=(Q(type=AuctionType.English) & Q(buy_now_price__isnull=False) & Q(
                    update_frequency__isnull=True)) & Q(bid_step__isnull=True) |
                      (Q(type=AuctionType.Dutch) & Q(update_frequency__isnull=False) & Q(
                          buy_now_price__isnull=True) & Q(bid_step__isnull=False)),
                name='auction_fields_check'
            ),

        ]
