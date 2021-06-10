from .models import Item
from .serializers import ItemSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated


class ItemListCreateView(ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    # permission_classes = [IsAuthenticated]


class ItemRetrieveView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    # permission_classes = [IsAuthenticated]
