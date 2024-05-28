from django.http import JsonResponse
from generos.models import Genero

def genero_view(request):
    generos = Genero.objects.all()
    data = [{'id': genero.id, 'nome': genero.nome} for genero in generos]
    return JsonResponse(data, safe=False)