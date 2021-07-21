from .models import Offer
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from .serializers import OfferSerializer
from rest_framework.filters import SearchFilter


class OfferCreateViewSet(GenericViewSet, CreateModelMixin, ListModelMixin):
    queryset = Offer.objects.all().order_by('-id')
    serializer_class = OfferSerializer
    filter_backends = [SearchFilter]
    search_fields = ['=auction__id']
