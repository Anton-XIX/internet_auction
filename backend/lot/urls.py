from .views import LotListCreateRetrieveViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'lot', LotListCreateRetrieveViewSet, basename='lot')
urlpatterns = router.urls
