from .models import Offer
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from .serializers import OfferSerializer


class OfferCreateViewSet(GenericViewSet, CreateModelMixin, ListModelMixin):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
