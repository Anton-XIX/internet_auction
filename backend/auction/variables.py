import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _


DEACTIVATION_PERIOD = datetime.timedelta(seconds=10)


class AuctionType(models.TextChoices):
    English = 'En', _('English')
    Dutch = 'Nl', _('Dutch')


