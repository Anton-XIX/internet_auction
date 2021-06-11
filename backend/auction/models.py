from django.db import models


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
    update_frequency = models.DurationField()
    duration = models.DurationField()
    current_price = models.DecimalField(max_digits=8, decimal_places=2)

    # class Meta:
    #     constraints = models.UniqueConstraint(fields=['user'], condition=Q(status='DRAFT'), name='unique_draft_user')
#
#
