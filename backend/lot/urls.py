from .views import LotListCreateRetrieveViewSet, OfferCreateViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'lot', LotListCreateRetrieveViewSet, basename='lot')
router.register(r'offer', OfferCreateViewSet, basename='offer')
urlpatterns = router.urls
