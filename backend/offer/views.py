from .models import Offer
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from .serializers import OfferSerializer
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class OfferCreateViewSet(GenericViewSet, CreateModelMixin, ListModelMixin):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Offer.objects.all().order_by('-id')
    serializer_class = OfferSerializer
    filter_backends = [SearchFilter]
    search_fields = ['=auction__id']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
