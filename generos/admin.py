from django.contrib import admin
from generos.models import Genero


@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('id', 'nome')




