from django.shortcuts import render,redirect,get_object_or_404
from .models import Viagem
from caravana.utils.sql_to_table import SqlToTable
# Create your views here.
def viagem_index(request):
    return render(request, 'viagem_index.html')

def viagem_form(request, id=None):
    obj_viagem = Viagem()
    if id:
        obj_viagem = get_object_or_404(Viagem, pk=id)

    return render(request, 'viagem_form.html', {'obj_viagem': obj_viagem})


def viagem_delete(request,id=None):
    if id:
        obj_viagem = get_object_or_404(Viagem, pk=id)
        obj_viagem.status = 0
        obj_viagem.save()

    return redirect('viagem:list_all')

def viagem_list_all(request):
    id_usuario = request.user.id
    query = "select id,nome as Viagem,date_format(data,'%%d/%%m/%%Y') as Data,hora_partida as Hora,Origem,Destino from viagem_viagem where status > 0 and cod_usuario_id = %s order by data"
    params = [id_usuario]
    params = [5] 

    print(params)

   
    try:
        obj_sql_to_table = SqlToTable()
        obj_sql_to_table.set_query(query)
        obj_sql_to_table.set_params(params)
    except Exception as e:
        print('Erro ao criar objeto SqlToTable: ', e)


    obj_sql_to_table.set_edit_rout('viagem:form_edit')
    obj_sql_to_table.set_delete_rout('viagem:delete')
    table = obj_sql_to_table.query_to_html()
    return render(request, 'viagem_list_all.html',{'table':table})

from django.shortcuts import render, redirect
from .models import Viagem

def viagem_save(request):

    cod_usuario = request.user.id

    if request.method == 'POST':
        id = request.POST.get('id')
        if id.isdigit():
            obj_viagem = get_object_or_404(Viagem, pk=id)
        else:
            obj_viagem = Viagem()

       # Preenche os campos
        obj_viagem.nome = request.POST.get('nome')
        obj_viagem.data = request.POST.get('data')
        obj_viagem.hora_partida = request.POST.get('hora_partida')
        obj_viagem.hora_chegada = request.POST.get('hora_chegada')
        obj_viagem.local_partida = request.POST.get('local_partida')
        obj_viagem.origem = request.POST.get('origem')
        obj_viagem.destino = request.POST.get('destino')
        obj_viagem.preco = request.POST.get('preco')
        obj_viagem.descricao = request.POST.get('descricao')
        obj_viagem.obs = request.POST.get('obs')
        obj_viagem.acentos_andar1d = request.POST.get('acentos_andar1d')
        obj_viagem.acentos_andar1e = request.POST.get('acentos_andar1e')
        obj_viagem.acentos_andar2d = request.POST.get('acentos_andar2d')
        obj_viagem.acentos_andar2e = request.POST.get('acentos_andar2e')
        obj_viagem.cod_usuario_id = cod_usuario

        obj_viagem.save()

        return redirect('viagem:list_all')  # redireciona pra alguma lista de viagens, por exemplo


def viagem_find(request):
    return render(request, 'viagem_find.html')



