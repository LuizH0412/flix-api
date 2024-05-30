from django.db import models

NACIONALIDADES = (
    ('USA', 'Estados Unidos da América'),
    ('BRA', 'Brasil'),
    ('DEU', 'Alemanha'),
    ('GBR', 'Inglaterra'),
    ('CAN', 'Canáda'),
    ('FRA', 'França'),
    ('PRT', 'Portugal'),
    ('ESP', 'Espanha'),
    ('ARG', 'Argentina'),
    ('ITA', 'Itália'),
    ('URY', 'Uruguai'),
    ('MEX', 'México'),
    ('OTHER', 'Outros')
)

class Ator(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField(null=True, blank=True)
    nacionalidade = models.CharField(
        max_length=200,
        choices=NACIONALIDADES,
        blank=True,
        null=True
        )


    def __str__(self):
        return self.nome