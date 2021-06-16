from django.urls import path

from .views import LotListCreateView, LotRetrieveView, LotCreateTestView

urlpatterns = [
    path('lot/', LotListCreateView.as_view()),
    path('lot_test/', LotCreateTestView.as_view()),
    path('lot/<int:pk>', LotRetrieveView.as_view()),
]
