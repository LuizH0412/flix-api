from django.db import models
from atores.models import Ator
from generos.models import Genero


class Filme(models.Model):
    titulo = models.CharField(max_length=500)
    genero = models.ForeignKey(
        Genero, 
        on_delete=models.PROTECT,
        related_name='genero_filme')
    data_lancamento = models.DateField(null=True, blank=True)
    atores = models.ManyToManyField(Ator, related_name='ator_filme')
    resumo = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.titulo
    

