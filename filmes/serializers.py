from rest_framework import serializers
from filmes.models import Filme

class FilmesSerializer(serializers.ModelSerializer):
    media = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Filme
        fields = '__all__'

    
    def get_media(self, obj):
        reviews = obj.filme_review.all() 
        if not reviews:
            return 0
        media = sum([review.estrelas for review in reviews]) / reviews.count()
        return round(media, 2)


    def validate_data_lancamento(self, value):
        if value.year < 1964:
            raise serializers.ValidationError('A data de lançamento não pode ser anterior a 1990')
        else:
            return value