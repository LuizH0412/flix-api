from atores.models import Ator
from rest_framework import generics
from atores.serializers import AtorSerializer


class AtorCreateListView(generics.ListCreateAPIView):
    queryset = Ator.objects.all()
    serializer_class = AtorSerializer


class AtorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ator.objects.all()
    serializer_class = AtorSerializer





