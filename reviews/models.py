from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from filmes.models import Filme


class Review(models.Model):
    filme = models.ForeignKey(
        Filme,
        on_delete=models.PROTECT, 
        related_name='filme_review')
    estrelas = models.IntegerField(
        validators= [
            MinValueValidator(0, 'A avaliação não pode ser inferior a 0 estrelas.'),
            MaxValueValidator(5, 'A avaliação não pode ser superior a 5 estrelas.')
        ]
    )
    comentario = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.comentario