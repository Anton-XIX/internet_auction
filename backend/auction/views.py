from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from .serializers import AuctionSerializer
from .models import Auction


class AuctionListCreateRetrieveViewSet(GenericViewSet, ListModelMixin,
                                       CreateModelMixin, RetrieveModelMixin,
                                       UpdateModelMixin):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer
    http_method_names = ['get', 'post', 'head', 'patch']
    # permission_classes = [IsAuthenticated]
