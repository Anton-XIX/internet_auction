from django.contrib import admin
from .models import Auction
from .utils import duration_to_seconds
from .variables import AuctionType
import datetime
import random


class AuctionAdmin(admin.ModelAdmin):
    model = Auction

    actions = ['start_updating_auctions', 'activate_auctions_for_testing']

    def activate_auctions_for_testing(self, request, queryset):
        queryset.update(is_active=True,
                        end_date=datetime.datetime.now() + datetime.timedelta(seconds=random.randint(2, 5)))

    def start_updating_auctions(self, request, queryset):
        from .tasks import price_changer
        invalid_auctions = []
        success_auctions = []
        for obj in queryset:
            if obj.type == AuctionType.Dutch:
                price_changer.apply_async(args=[obj.pk, obj.bid_step, duration_to_seconds(obj.update_frequency)],
                                          countdown=duration_to_seconds(obj.update_frequency))
                success_auctions.append(str(obj.pk))
            else:
                invalid_auctions.append(str(obj.pk))
        if invalid_auctions:
            self.message_user(request, f'{",".join(invalid_auctions)} - Invalid auction type. Updating price was not '
                                       f'started')
        else:
            self.message_user(request, f'Successfully started updating price for {success_auctions} auctions')


admin.site.register(Auction, AuctionAdmin)
