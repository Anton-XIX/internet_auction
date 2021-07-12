from django.contrib import admin
from .models import Auction
from .utils import duration_to_seconds
from .variables import AuctionType
from .models import AuctionManager
from django.utils.translation import ngettext


class AuctionAdmin(admin.ModelAdmin):
    model = Auction

    actions = ['start_updating_auctions']

    def start_updating_auctions(self, request, queryset):
        from .tasks import price_changer
        invalid_auctions = []
        for obj in queryset:
            if obj.type == AuctionType.Dutch:
                price_changer.apply_async(args=[obj.pk, obj.bid_step, duration_to_seconds(obj.update_frequency)],
                                          countdown=duration_to_seconds(obj.update_frequency))
            else:
                invalid_auctions.append(str(obj.pk))
        if invalid_auctions:
            self.message_user(request, f'{",".join(invalid_auctions)} - Invalid auction type. Updating price was not '
                                       f'started')
        else:
            self.message_user(request, f'Successfully started updating price for selected auctions')


admin.site.register(Auction, AuctionAdmin)
