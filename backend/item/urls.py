from .views import ItemListCreateRetrieveViewSet
from rest_framework.routers import DefaultRouter
from helpers.url_base import UrlBase

router = DefaultRouter()
router.register(r'item', ItemListCreateRetrieveViewSet, basename=UrlBase.item)
urlpatterns = router.urls
