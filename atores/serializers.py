from rest_framework import serializers
from atores.models import Ator

class AtorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ator
        fields = '__all__'