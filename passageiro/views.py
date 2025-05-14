from django.shortcuts import redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import render
from .models import passageiro
import logging
import json


def passageiro_save(request):
    try:
        id = request.POST.get('id')
        nome = request.POST.get('nome')
        rua = request.POST.get('rua')
        numero = request.POST.get('numero')
        cep = request.POST.get('cep')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')
        status = request.POST.get('status')
        obs = request.POST.get('obs')

        if id:
            obj_passageiro =  get_object_or_404(passageiro,id=id)
        else:
            obj_passageiro = passageiro()

        obj_passageiro.id = id
        obj_passageiro.nome = nome
        obj_passageiro.rua = rua
        obj_passageiro.numero = numero
        obj_passageiro.cep = cep
        obj_passageiro.cidade = cidade
        obj_passageiro.estado = estado
        obj_passageiro.status = status
        obj_passageiro.obs = obs

        obj_passageiro.save()

        return JsonResponse({'return': 'success', 'message': 'Saved successfully.'})

    except Exception as e:    
        logging.error(f"Error saving: {e}")
        return JsonResponse({'error': str(e)}, status=500)

    
@require_POST
def passageiro_delete(request):
    try:
        data = json.loads(request.body)
        passageiro_id = data.get('id')
        obj_passageiro = passageiro.objects.get(id=passageiro_id)
        obj_passageiro.status = 0
        obj_passageiro.save()
        return JsonResponse({'return': 'success', 'message': 'Deleted successfully.'}, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
    


def passageiro_form(request, id=None):
    obj_passageiro = passageiro()
    if id:
        obj_passageiro = get_object_or_404(passageiro, pk=id)


    return render(request, 'passageiro_form.html', {'obj_passageiro': obj_passageiro})    