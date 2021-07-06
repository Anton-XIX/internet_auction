from .views import OfferCreateViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'offer', OfferCreateViewSet, basename='offer')
urlpatterns = router.urls
