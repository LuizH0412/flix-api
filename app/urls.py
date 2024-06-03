from django.contrib import admin
from django.urls import path
from generos.views import GeneroCreateListView, GeneroRetrieveUpdateDestroyAPIView
from atores.views import AtorCreateListView, AtorRetrieveUpdateDestroyAPIView
from filmes.views import FilmesCreateListView, FilmesRetrieveUpdateDestroyAPIView
from reviews.views import ReviewListCreateView, ReviewRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('generos/', GeneroCreateListView.as_view(), name='genero'),
    path('generos/<int:pk>/', GeneroRetrieveUpdateDestroyAPIView.as_view(), name='detail-genero'),

    path('atores/', AtorCreateListView.as_view(), name='atores'),
    path('atores/<int:pk>/', AtorRetrieveUpdateDestroyAPIView.as_view(), name='detail-atores'),

    path('filmes/', FilmesCreateListView.as_view(), name='filmes'),
    path('filmes/<int:pk>/', FilmesRetrieveUpdateDestroyAPIView.as_view(), name='filmes-detail'),

    path('reviews/', ReviewListCreateView.as_view(), name='reviews'),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDestroyAPIView.as_view(), name='reviews-detail'),
]
