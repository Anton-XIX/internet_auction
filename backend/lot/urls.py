from django.urls import path

from .views import LotListCreateView, LotRetrieveView, LotListCreateTestView

urlpatterns = [
    path('lot/', LotListCreateView.as_view()),
    path('lot_test/', LotListCreateTestView.as_view()),
    path('lot/<int:pk>', LotRetrieveView.as_view()),
]
