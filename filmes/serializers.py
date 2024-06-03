from rest_framework import serializers
from filmes.models import Filme

class FilmesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filme
        fields = '__all__'