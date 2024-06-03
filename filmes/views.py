from rest_framework import generics
from filmes.models import Filme
from filmes.serializers import FilmesSerializer


class FilmesCreateListView(generics.ListCreateAPIView):
    queryset = Filme.objects.all()
    serializer_class = FilmesSerializer


class FilmesRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Filme.objects.all()
    serializer_class = FilmesSerializer
