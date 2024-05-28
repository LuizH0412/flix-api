from django.contrib import admin
from django.urls import path
from generos.views import genero_create_list_view,genero_detail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('generos/', genero_create_list_view, name='genero'),
    path('generos/<int:pk>/', genero_detail_view, name='detail-genero')
]
