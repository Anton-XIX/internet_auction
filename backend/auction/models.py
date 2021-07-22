import datetime

from django.db.models import Q
from django.db import models

from .utils import duration_to_seconds
from .variables import AuctionType

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


class AuctionManager(models.Manager):
    use_in_migrations = True

    def create(self, *args, **kwargs):
        obj = super(AuctionManager, self).create(*args, **kwargs)
        if obj.type == AuctionType.Dutch:
            from .tasks import price_changer
            price_changer.apply_async(args=[obj.pk, obj.bid_step, duration_to_seconds(obj.update_frequency)],
                                      countdown=duration_to_seconds(obj.update_frequency))
        return obj


class Auction(models.Model):
    type = models.CharField(max_length=20, choices=AuctionType.choices)
    start_price = models.DecimalField(max_digits=8, decimal_places=2)
    reserve_price = models.DecimalField(max_digits=8, decimal_places=2)

    end_date = models.DateTimeField(null=True, blank=True)
    current_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    update_frequency = models.DurationField(blank=True, null=True)

    bid_step = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    buy_now_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    is_buy_now_available = models.BooleanField(default=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    objects = AuctionManager()

    def __str__(self):
        return f'{self.type} - {self.pk}'

    def deactivate_auction(self):
        self.is_active = False
        self.save(update_fields=['is_active'])

    def save(self, *args, **kwargs):
        if not self.current_price:
            self.current_price = self.start_price

        super().save(*args, **kwargs)

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


'''Signal calls task for Dutch auction only on creating: signal checks attribute 'created': True if instance is 
creating  and False if instance was created '''

# @receiver(post_save, sender=Auction)
# def my_handler(sender, instance, created, **kwargs):
#     if created and instance.type == AuctionType.Dutch:
#         from .tasks import price_changer
#         price_changer.apply_async(args=[instance.pk, instance.bid_step, instance.duration],
#                                   countdown=duration_to_seconds(instance.duration))
