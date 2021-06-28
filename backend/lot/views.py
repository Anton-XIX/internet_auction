from .models import Lot, Offer
from .serializers import LotNestedSerializer, OfferSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin

'''Search field and type(=, ^ etc.) ?'''


class LotListCreateRetrieveViewSet(GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin):
    queryset = Lot.objects.all()
    serializer_class = LotNestedSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['item__title']
    ordering_fields = ['duration', 'current_price']


class OfferCreateViewSet(GenericViewSet, CreateModelMixin):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
