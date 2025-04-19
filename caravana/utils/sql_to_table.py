from django.db import connections
from django.utils.html import escape

class SqlToTable:
    def __init__(self):
        self.query = None
        self.params = None
        self.edit_rout = None
        self.delete_rout = None

    def set_query(self, query):
        self.query = query


    def set_params(self, params):
        self.params = params

    def set_edit_rout(self, edit_rout):
        self.edit_rout = edit_rout

    def set_delete_rout(self, delete_rout):
        self.delete_rout = delete_rout

    def execute_query(self):
        # Utilizando a conexão do Django
        with connections['default'].cursor() as cursor:
            cursor.execute(self.query, self.params)
            result = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]  # Agora dentro do with
        return result, columns

    def get_buttons(self):
        if self.edit_rout != None:
            buttons = f'<a href="{self.edit_rout}" class="btn btn-primary">Editar</a>'

        if self.delete_rout != None:
            buttons += f'<a href="{self.delete_rout}" class="btn btn-danger">Excluir</a>'

        return buttons

    def query_to_html(self):
        result, columns = self.execute_query()

        # Adicionando os botões de editar e excluir
        buttons = self.get_buttons()

        # Criando a tabela HTML com Bootstrap
        table_html = '<table class="table table-bordered table-striped">'

        # Cabeçalhos
        table_html += '<thead><tr>'
        for column in columns:
            table_html += f'<th>{escape(column)}</th>'
        table_html += '</tr></thead>'

        # Corpo da tabela
        table_html += '<tbody>'
        for row in result:
            table_html += '<tr>'
            for column in row:
                table_html += f'<td>{escape(str(column))}</td>'
            table_html += f'<td>{buttons}</td></tr>'
        table_html += '</tbody>'

        table_html += '</table>'

        return table_html
