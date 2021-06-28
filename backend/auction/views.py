from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from .serializers import AuctionSerializer
from .models import Auction


class AuctionListCreateRetrieveViewSet(GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer
    # permission_classes = [IsAuthenticated]
