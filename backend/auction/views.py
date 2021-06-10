from .models import EnglishAuction, DutchAuction
from .serializers import EnglishAuctionSerializer, DutchAuctionSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated


class EnglishAuctionListCreateView(ListCreateAPIView):
    queryset = EnglishAuction.objects.all()
    serializer_class = EnglishAuctionSerializer
    # permission_classes = [IsAuthenticated]


class EnglishAuctionRetrieveView(RetrieveAPIView):
    queryset = EnglishAuction.objects.all()
    serializer_class = EnglishAuctionSerializer
    # permission_classes = [IsAuthenticated]


class DutchAuctionListCreateView(ListCreateAPIView):
    queryset = DutchAuction.objects.all()
    serializer_class = DutchAuctionSerializer
    # permission_classes = [IsAuthenticated]


class DutchAuctionRetrieveView(RetrieveAPIView):
    queryset = DutchAuction.objects.all()
    serializer_class = DutchAuctionSerializer
    # permission_classes = [IsAuthenticated]
