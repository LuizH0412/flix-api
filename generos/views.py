import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from generos.models import Genero

@csrf_exempt
def genero_create_list_view(request):
    if request.method == 'GET':
        generos = Genero.objects.all()
        data = [{'id': genero.id, 'nome': genero.nome} for genero in generos]
        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        novo_genero = Genero(nome=data['nome'])
        novo_genero.save()
        return JsonResponse({'id': novo_genero.id, 'nome': novo_genero.nome}, status=201)
    
@csrf_exempt
def genero_detail_view(request, pk):
    genero = get_object_or_404(Genero, pk=pk)

    if request.method == 'GET':
        data = {'id': genero.id, 'nome': genero.nome}
        return JsonResponse(data)
    
    elif request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))
        genero.nome = data['nome']
        genero.save()
        return JsonResponse({'id': genero.id, 'nome': genero.nome}, status=201)

    elif request.method == 'DELETE':
        genero.delete()
        return JsonResponse(
            {'mensagem': 'Gênero excluido com sucesso!'},
            status=204,
        )