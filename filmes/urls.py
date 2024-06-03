from django.urls import path
from . import views

urlpatterns = [
    path('filmes/', views.FilmesCreateListView.as_view(), name='filmes'),
    path('filmes/<int:pk>/', views.FilmesRetrieveUpdateDestroyAPIView.as_view(), name='filmes-detail'),
]