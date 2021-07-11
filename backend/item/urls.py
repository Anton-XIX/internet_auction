from django.urls import path

from .views import ItemListCreateView, ItemRetrieveView

urlpatterns = [
    path('item/', ItemListCreateView.as_view()),
    path('item/<int:pk>', ItemRetrieveView.as_view()),
]
