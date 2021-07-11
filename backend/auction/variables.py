from django.db import models
from django.utils.translation import gettext_lazy as _


class AuctionType(models.TextChoices):
    English = 'En', _('English')
    Dutch = 'Nl', _('Dutch')

