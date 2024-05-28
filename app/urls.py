from django.contrib import admin
from django.urls import path
from generos.views import genero_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('generos/', genero_view, name='genero-list'),
]
