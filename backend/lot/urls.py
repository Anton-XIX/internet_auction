from django.urls import path

from .views import LotListCreateView, LotRetrieveView

urlpatterns = [
    path('lot/', LotListCreateView.as_view()),
    path('lot/<int:pk>', LotRetrieveView.as_view()),
]
