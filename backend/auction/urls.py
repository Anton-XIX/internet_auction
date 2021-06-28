
from .views import AuctionListCreateRetrieveViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'auction', AuctionListCreateRetrieveViewSet, basename='auction')
urlpatterns = router.urls
