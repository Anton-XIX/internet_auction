from django.db import models
from django.db.models import Q


class Auction(models.Model):
    ENGLISH = 'En'
    DUTCH = 'Nl'
    AUCTION_TYPE = [
        (ENGLISH, 'English'),
        (DUTCH, 'Dutch'),
    ]

    type = models.CharField(max_length=20, choices=AUCTION_TYPE)
    start_price = models.DecimalField(max_digits=8, decimal_places=2)
    reserve_price = models.DecimalField(max_digits=8, decimal_places=2)
    duration = models.DurationField()
    update_frequency = models.DurationField(blank=True, null=True)
    current_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f'{self.type} - {self.pk}'

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=Q(type='En') & Q(current_price__isnull=False), name='en_auction'
            ),
            models.CheckConstraint(
                check=Q(type='Nl') & Q(update_frequency__isnull=False), name='nl_auction'
            ),
        ]

#
#
