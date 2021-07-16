from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/auction/<int:pk>', consumers.AuctionConsumer.as_asgi()),
    path('ws/auction/', consumers.AuctionConsumer.as_asgi()),
]