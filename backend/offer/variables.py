import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _


class OfferType(models.TextChoices):
    Bid = 'Bid', _('Bid')
    Buy = 'Buy', _('Byu now')
