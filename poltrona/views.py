from django.shortcuts import redirect, get_object_or_404
from django.db import connection
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Poltrona
from viagem.models import Viagem
from django.shortcuts import render
import logging
import json


# Create your views here.

def poltrona_add_all(request,id_viagem):
    
     if str(id_viagem).isdigit():
          obj_viagem =  get_object_or_404(Viagem,id=id_viagem)
          acentos_andar1d = obj_viagem.acentos_andar1d
          acentos_andar1e = obj_viagem.acentos_andar1e
         
          while acentos_andar1d > 0:
               obj_poltrona = Poltrona()
               obj_poltrona.cod_viagem = id_viagem
               obj_poltrona.nome = acentos_andar1d
               obj_poltrona.cod_passageiro = 0
               obj_poltrona.cod_pagamento = 0
               obj_poltrona.cod_usuario_id = 0
               obj_poltrona.status = 1
               
               obj_poltrona.save()

               acentos_andar1d = acentos_andar1d -1

          while acentos_andar1e > 0:
               obj_poltrona = Poltrona()
               obj_poltrona.cod_viagem = id_viagem
               obj_poltrona.nome = acentos_andar1e
               obj_poltrona.status = 1
               obj_poltrona.save()

               acentos_andar1e = acentos_andar1e -1     

     return JsonResponse({'return': 'success', 'message': 'Saved successfully.'})



def poltrona_list_all(request,id):    
    if str(id).isdigit():
          obj_viagem = get_object_or_404(Viagem,id=id)
          poltronas = Poltrona.objects.filter(cod_viagem=id).order_by('-id')
          context = {
               'poltronas': poltronas,
               'viagem': obj_viagem,
               'id': id
          }

        

          return render(request, 'poltrona/poltrona_list_all.html', context)
    else:
          return JsonResponse({'return': 'error', 'message': 'Invalid ID.'}) 
    

def poltrona_selecionou(request):    
     if request.method == 'POST':
        selecionadas = tuple(request.POST.getlist('cb_poltrona'))
        quantidade = len(selecionadas)
        selecionadas_in = str(selecionadas).replace(",)", ")")        
        
        if quantidade > 0:
               query = f"UPDATE poltrona_poltrona SET status = 3 WHERE id IN {selecionadas_in}"
               try:
                    with connection.cursor() as cursor:          
                         cursor.execute(query)
               except Exception as e:
                    logging.error(f"Error updating poltrona status: {e}")
                    return JsonResponse({'return': 'error', 'bg':'bg-danger' , 'message': 'Failed to update poltrona status.'})     
        else:
               return JsonResponse({'return': 'error', 'bg':'bg-warning' , 'message': 'Selecione ao menos uma poltrona.'}) 
         
        return JsonResponse({'return': 'success', 'bg':'bg-success' ,'message': 'Reserva realizada com sucesso.'})

         