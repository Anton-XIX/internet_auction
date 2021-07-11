from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from lot.models import Lot


class EnglishAuction(models.Model):
    start_price = models.DecimalField(max_digits=8, decimal_places=2)
    reserve_price = models.DecimalField(max_digits=8, decimal_places=2)
    current_price = models.DecimalField(max_digits=8, decimal_places=2)
    duration = models.DurationField()

    # lot = GenericRelation(Lot, content_type_field='content_type',
    #     object_id_field='object_id')


class DutchAuction(models.Model):
    objects = None
    start_price = models.DecimalField(max_digits=8, decimal_places=2)
    reserve_price = models.DecimalField(max_digits=8, decimal_places=2)
    update_frequency = models.DurationField()
    duration = models.DurationField()

    # lot = GenericRelation(Lot, content_type_field='content_type',
    #     object_id_field='object_id')
