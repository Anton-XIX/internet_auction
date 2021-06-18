from .models import Lot
from .serializers import LotSerializer, LotNestedSerializer, LotListTestSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter


class LotListCreateView(ListCreateAPIView):
    queryset = Lot.objects.all()
    serializer_class = LotSerializer
    # permission_classes = [IsAuthenticated]


class LotRetrieveView(RetrieveAPIView):
    queryset = Lot.objects.all()
    serializer_class = LotNestedSerializer
    # permission_classes = [IsAuthenticated]


'''Search field and type(=, ^ etc.) ?'''


class LotListCreateTestView(ListCreateAPIView):
    queryset = Lot.objects.all()
    serializer_class = LotNestedSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['item__title']
    ordering_fields = ['duration', 'current_price']


'''TESTING FUTURE FUNCTIONALITY'''


class LotListTestView(ListAPIView):
    queryset = Lot.objects.all()
    serializer_class = LotListTestSerializer
