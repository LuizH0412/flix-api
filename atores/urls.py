from django.urls import path
from . import views


urlpatterns = [
    path('atores/', views.AtorCreateListView.as_view(), name='atores'),
    path('atores/<int:pk>/', views.AtorRetrieveUpdateDestroyAPIView.as_view(), name='detail-atores'),
]