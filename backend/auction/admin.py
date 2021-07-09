from django.contrib import admin
from .models import Auction
from .utils import duration_to_seconds


class AuctionAdmin(admin.ModelAdmin):
    model = Auction

    actions = ['delete_payment_info']

    def start_updating_price(self, request, queryset):
        from .tasks import price_changer
        for obj in queryset:
            if not obj.type == 'Nl':  # replace
                raise Exception('Invalid auction type choice')
            price_changer.apply_async(args=[obj.pk, obj.bid_step, duration_to_seconds(obj.duration)],
                                      countdown=duration_to_seconds(obj.duration))


admin.site.register(Auction, AuctionAdmin)
