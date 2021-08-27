from .views import AuctionListCreateRetrieveViewSet
from rest_framework.routers import DefaultRouter
from helpers.url_base import UrlBase

router = DefaultRouter()
router.register(r'auction', AuctionListCreateRetrieveViewSet, basename=UrlBase.auction)
urlpatterns = router.urls
