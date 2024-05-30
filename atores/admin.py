from django.contrib import admin
from atores.models import Ator


@admin.register(Ator)
class AtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'data_nascimento', 'nacionalidade')
    search_fields = ('id', 'nome', 'data_nascimento', 'nacionalidade')

