from .models import Lot
from .serializers import LotNestedSerializer, LotRetrieveSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter

'''Search field and type(=, ^ etc.) ?'''


class LotListCreateView(ListCreateAPIView):
    queryset = Lot.objects.all()
    serializer_class = LotNestedSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['item__title']
    ordering_fields = ['duration', 'current_price']


class LotRetrieveView(RetrieveAPIView):
    queryset = Lot.objects.all()
    serializer_class = LotRetrieveSerializer
