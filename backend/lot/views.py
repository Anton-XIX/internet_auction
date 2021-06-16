from .models import Lot
from .serializers import LotSerializer, LotNestedSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated


class LotListCreateView(ListCreateAPIView):
    queryset = Lot.objects.all()
    serializer_class = LotSerializer
    # permission_classes = [IsAuthenticated]


class LotRetrieveView(RetrieveAPIView):
    queryset = Lot.objects.all()
    serializer_class = LotSerializer
    # permission_classes = [IsAuthenticated]


class LotCreateTestView(CreateAPIView):
    queryset = Lot.objects.all()
    serializer_class = LotNestedSerializer