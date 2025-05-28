from django.shortcuts import render,redirect,get_object_or_404
from .models import Viagem
from poltrona.views import poltrona_add_all
from caravana.utils.sql_to_table import SqlToTable
from django.shortcuts import render, redirect
from django.db import connection
from django.http import HttpResponse
from django.http import JsonResponse




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



def viagem_save(request):

    cod_usuario = request.user.id

    if request.method == 'POST':
        id = request.POST.get('id')
        add = 0
        if id.isdigit():
            obj_viagem = get_object_or_404(Viagem, pk=id)
        else:
            obj_viagem = Viagem()
            add = 1

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
        id_viagem = obj_viagem.id

        if (add == 1):
            poltrona_add_all(request,id_viagem)


    return redirect('viagem:list_all')  # redireciona pra alguma lista de viagens, por exemplo


def viagem_find(request):
    return render(request, 'viagem_find.html')

def viagem_origem_options(request):
    query = """
        SELECT MIN(id) AS id, origem
        FROM viagem_viagem
        WHERE DATA >= CURDATE()
        AND (
            (DATA = CURDATE() AND hora_partida >= CURTIME())
            OR (DATA > CURDATE())
        )
        AND STATUS > 0
        GROUP BY origem
        ORDER BY origem;

    """

    with connection.cursor() as cursor:  
        cursor.execute(query)
        rows = cursor.fetchall()

        result = ""
        for row in rows:           
            result += f"<option value='{row[1]}'>{row[1]}</option>"
    
    return HttpResponse(result)    


def viagem_destino_options(request):
    query = """
        SELECT MIN(id) AS id, destino
        FROM viagem_viagem
        WHERE DATA >= CURDATE()
        AND (
            (DATA = CURDATE() AND hora_partida >= CURTIME())
            OR (DATA > CURDATE())
        )
        AND STATUS > 0
        GROUP BY destino
        ORDER BY destino;

    """

    with connection.cursor() as cursor:  
        cursor.execute(query)
        rows = cursor.fetchall()

        result = ""
        for row in rows:           
            result += f"<option value='{row[1]}'>{row[1]}</option>"
    
    return HttpResponse(result) 




def viagem_sql_find(request):
    origem = request.POST.get('origem')
    destino = request.POST.get('destino')
    data  = request.POST.get('partida')
  

    query = """
            SELECT 
            id,
            Origem,
            Destino,
            date_format(data,'%%d/%%m/%%Y') as Partida,           
            preco as Preço,
            descricao as Descrição,
            Obs
            FROM viagem_viagem
            WHERE
            (data >= curdate() OR
            (data = curdate() and hora_partida > curtime())) AND
            
        """    

    if not data:      
        query +=""" origem = %s AND
                    destino = %s
                    order by data,hora_partida
                """   
        params = [origem,destino]
        
                 
    else:

        query +=""" origem = %s AND
                    destino = %s AND
                    data = %s
                    order by data,hora_partida
                """   
        params = [origem,destino,data]
        
    obj_sqltotable = SqlToTable()
    obj_sqltotable.set_query(query)
    obj_sqltotable.set_params(params)
    obj_sqltotable.set_edit_rout('poltrona:list_all')
    obj_sqltotable.execute_query()

    result = obj_sqltotable.query_to_html()

    return JsonResponse({"tabela": result})