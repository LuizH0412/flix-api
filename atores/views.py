from atores.models import Ator
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from atores.serializers import AtorSerializer


class AtorCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Ator.objects.all()
    serializer_class = AtorSerializer


class AtorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Ator.objects.all()
    serializer_class = AtorSerializer





