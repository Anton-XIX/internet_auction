from .views import OfferCreateViewSet
from rest_framework.routers import DefaultRouter
from helpers.url_base import UrlBase

router = DefaultRouter()
router.register(r'offer', OfferCreateViewSet, basename=UrlBase.offer)
urlpatterns = router.urls
