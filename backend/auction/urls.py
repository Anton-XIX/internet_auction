from django.urls import path

from .views import DutchAuctionListCreateView, DutchAuctionRetrieveView, \
                    EnglishAuctionListCreateView, EnglishAuctionRetrieveView
urlpatterns = [
    path('dutch_auction/', DutchAuctionListCreateView.as_view()),
    path('dutch_auction/<int:pk>', DutchAuctionRetrieveView.as_view()),
    path('english_auction', EnglishAuctionListCreateView.as_view()),
    path('english_auction/<int:pk>', EnglishAuctionRetrieveView.as_view()),

    ]