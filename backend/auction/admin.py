from django.contrib import admin
from .models import Auction
from .utils import duration_to_seconds
from .variables import AuctionType


class AuctionAdmin(admin.ModelAdmin):
    model = Auction

    actions = ['start_updating_auctions']

    def start_updating_price(self, request, queryset):
        from .tasks import price_changer
        for obj in queryset:
            if not obj.type == AuctionType.Dutch:
                raise ValueError('Invalid auction type choice')
            price_changer.apply_async(args=[obj.pk, obj.bid_step, duration_to_seconds(obj.update_frequency)],
                                      countdown=duration_to_seconds(obj.update_frequency))


admin.site.register(Auction, AuctionAdmin)
