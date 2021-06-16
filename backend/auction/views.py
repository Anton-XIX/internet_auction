from .models import Auction
from .serializers import AuctionSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated


class AuctionListCreateView(ListCreateAPIView):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer
    # permission_classes = [IsAuthenticated]


class AuctionRetrieveView(RetrieveAPIView):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer

    # permission_classes = [IsAuthenticated]
