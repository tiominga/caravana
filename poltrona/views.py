from django.shortcuts import redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Poltrona
from viagem.models import Viagem
from django.shortcuts import render
import logging
import json


# Create your views here.

def poltrona_add_all(request,id_viagem):
     print(id_viagem)
     if str(id_viagem).isdigit():
          obj_viagem =  get_object_or_404(Viagem,id=id_viagem)
          acentos_andar1d = obj_viagem.acentos_andar1d
          acentos_andar1e = obj_viagem.acentos_andar1e
          print("acentos andar1d"+str(acentos_andar1d))
          print("acentos_andar1e"+str(acentos_andar1e))
          while acentos_andar1d > 0:
               obj_poltrona = Poltrona()
               obj_poltrona.cod_viagem = id_viagem
               obj_poltrona.nome = acentos_andar1d
               obj_poltrona.cod_passageiro = 0
               obj_poltrona.cod_pagamento = 0
               obj_poltrona.cod_usuario_id = 0
               obj_poltrona.status = 1
               print(f"cod_passageiro = {obj_poltrona.cod_passageiro}")

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
    print('listarei as pontronas '+str(id))
    return JsonResponse({'return': 'success', 'message': 'Saved successfully.'})