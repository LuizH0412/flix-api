from generos.models import Genero
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from generos.serializers import GeneroSerializer



class GeneroCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer


class GeneroRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer
    