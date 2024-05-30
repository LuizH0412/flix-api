from django.contrib import admin
from django.urls import path
from generos.views import GeneroCreateListView, GeneroRetrieveUpdateDestroyAPIView
from atores.views import AtorCreateListView, AtorRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('generos/', GeneroCreateListView.as_view(), name='genero'),
    path('generos/<int:pk>/', GeneroRetrieveUpdateDestroyAPIView.as_view(), name='detail-genero'),
    path('atores/', AtorCreateListView.as_view(), name='atores'),
    path('atores/<int:pk>/', AtorRetrieveUpdateDestroyAPIView.as_view(), name='detail-atores'),
]
