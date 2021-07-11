from django.contrib import admin
from .models import EnglishAuction
from .models import DutchAuction

admin.site.register(EnglishAuction)
admin.site.register(DutchAuction)
