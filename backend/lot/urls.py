from .views import LotListCreateRetrieveViewSet
from rest_framework.routers import DefaultRouter
from helpers.url_base import UrlBase

router = DefaultRouter()
router.register(r'lot', LotListCreateRetrieveViewSet, basename=UrlBase.lot)
urlpatterns = router.urls
