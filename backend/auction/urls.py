from django.urls import path
from .views import AuctionListCreateView, AuctionRetrieveView

urlpatterns = [
    path('auction', AuctionListCreateView.as_view()),
    path('auction/<int:pk>', AuctionRetrieveView.as_view()),

    ]