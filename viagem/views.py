from django.shortcuts import render,redirect
from .models import Viagem
from caravana.utils.sql_to_table import SqlToTable

# Create your views here.
def viagem_index(request):
    return render(request, 'viagem_index.html')

def viagem_form(request):
    return render(request, 'viagem_form.html')

def viagem_find(request):
    id_usuario = request.user.id
    query = "select id as Cod,nome as Viagem,date_format(data,'%%d/%%m/%%Y') as Data,hora_partida as Hora,Origem,Destino from viagem_viagem where cod_usuario_id = %s order by data"
    params = [id_usuario]

    obj_sql_to_table = SqlToTable()
    obj_sql_to_table.set_query(query)
    obj_sql_to_table.set_params(params)
    obj_sql_to_table.set_edit_rout('viagem:form')
    obj_sql_to_table.set_delete_rout('viagem:delete')
    table = obj_sql_to_table.query_to_html()
    return render(request, 'viagem_find.html',{'table':table})

from django.shortcuts import render, redirect
from .models import Viagem

def viagem_save(request):

    cod_usuario = request.user.id

    if request.method == 'POST':
        nome = request.POST.get('nome')
        data = request.POST.get('data')
        hora_partida = request.POST.get('hora_partida')
        hora_chegada = request.POST.get('hora_chegada')
        local_partida = request.POST.get('local_partida')
        origem = request.POST.get('origem')
        destino = request.POST.get('destino')
        preco = request.POST.get('preco')
        descricao = request.POST.get('descricao')
        obs = request.POST.get('obs')
        acentos_andar1d = request.POST.get('acentos_andar1d')
        acentos_andar1e = request.POST.get('acentos_andar1e')
        acentos_andar2d = request.POST.get('acentos_andar2d')
        acentos_andar2e = request.POST.get('acentos_andar2e')

        # Cria e salva o objeto com os dados do formulário
        obj_viagem = Viagem(
            nome=nome,
            data=data,
            hora_partida=hora_partida,
            hora_chegada=hora_chegada,
            local_partida=local_partida,
            origem=origem,
            destino=destino,
            preco=preco,
            descricao=descricao,
            obs=obs,
            acentos_andar1d=acentos_andar1d,
            acentos_andar1e=acentos_andar1e,
            acentos_andar2d=acentos_andar2d,
            acentos_andar2e=acentos_andar2e,
            cod_usuario_id=cod_usuario,  # Relaciona com o usuário logado
        )
        obj_viagem.save()

        return redirect('viagem:find')  # redireciona pra alguma lista de viagens, por exemplo





