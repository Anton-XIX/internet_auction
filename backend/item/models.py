from django.db import models

from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True)
    photo = models.ImageField(upload_to='items/')

    def __str__(self):
        return self.title
