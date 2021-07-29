from .models import Lot
from .serializers import LotNestedSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status

'''Search field and type(=, ^ etc.) ?'''


class LotListCreateRetrieveViewSet(GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin):
    # parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticated]
    queryset = Lot.objects.select_related('auction', 'item')
    serializer_class = LotNestedSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['item__title']
    ordering_fields = ['duration', 'current_price']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



