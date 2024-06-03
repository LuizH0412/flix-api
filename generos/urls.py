from django.urls import path
from . import views

urlpatterns = [
    path('generos/', views.GeneroCreateListView.as_view(), name='genero'),
    path('generos/<int:pk>/', views.GeneroRetrieveUpdateDestroyAPIView.as_view(), name='detail-genero'),
]