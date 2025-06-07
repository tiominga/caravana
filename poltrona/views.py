from django.shortcuts import redirect, get_object_or_404
from django.db import connection
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Poltrona
from pedido.models import Pedido
from viagem.models import Viagem
from django.shortcuts import render
import logging
import json
import uuid
from django.contrib.auth.decorators import login_required

@login_required


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
    

def poltrona_pedido(id_poltrona,grupo):
    if str(id_poltrona).isdigit():
        obj_pedido = Pedido()      
        obj_pedido.cod_poltrona_id = id_poltrona
        obj_pedido.id_pagamento = 'Aberto'
        obj_pedido.forma_pagamento = 'Aberto'
        obj_pedido.grupo = grupo
        obj_pedido.status = 1
        obj_pedido.save()

        return JsonResponse({'return': 'success', 'message': 'Pedido created successfully.'})
    else:
        return JsonResponse({'return': 'error', 'message': 'Invalid Poltrona ID.'})    
    

def poltrona_selecionou(request):    
     if request.method == 'POST':
        selecionadas = tuple(request.POST.getlist('cb_poltrona'))
        quantidade = len(selecionadas)
        selecionadas_in = str(selecionadas).replace(",)", ")") 

        cod_usuario = request.user.id       
        
        if quantidade > 0:
               query = f"UPDATE poltrona_poltrona SET status = 3,cod_usuario_id = {cod_usuario} WHERE id IN {selecionadas_in}"              
               try:
                    with connection.cursor() as cursor:          
                         cursor.execute(query)
                         grupo = uuid.uuid4().hex[:12]
                         for selecionadas in selecionadas:
                              poltrona_pedido(selecionadas,grupo)
               except Exception as e:
                    logging.error(f"Error updating poltrona status: {e}")
                    return JsonResponse({'return': 'error', 'bg':'bg-danger' , 'message': 'Falha, parece que você precisa se logar novamente...','redirect':'None'})     
        else:
               return JsonResponse({'return': 'error', 'bg':'bg-warning' , 'message': 'Selecione ao menos uma poltrona.','redirect':'None'}) 
        
        return JsonResponse({'return': 'success', 'bg':'bg-success' ,'message': 'Reserva realizada com sucesso. Aguarde...','redirect':'/passageiro/form/'})        