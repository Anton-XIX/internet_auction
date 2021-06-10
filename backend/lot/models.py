from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from item.models import Item


class Lot(models.Model):
    AUCTION_TYPE = [
        ('En', 'English'),
        ('Nl', 'Dutch'),
    ]

    item = models.OneToOneField(Item, on_delete=models.CASCADE)
    auction_type = models.CharField(choices=AUCTION_TYPE, max_length=100)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')