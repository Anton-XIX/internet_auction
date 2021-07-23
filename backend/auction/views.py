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

    # @action(detail=True, methods=['post'], url_name='buy_now_lot')
    # def buy(self, request, pk):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance=instance, data=self.request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response()