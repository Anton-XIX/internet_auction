from .views import ItemListCreateRetrieveViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'item', ItemListCreateRetrieveViewSet, basename='item')
urlpatterns = router.urls
