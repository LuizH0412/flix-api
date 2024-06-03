from django.contrib import admin
from filmes.models import Filme


@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'genero', 'data_lancamento', 'resumo')
