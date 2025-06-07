from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pedido(models.Model):    
    cod_poltrona = models.ForeignKey('poltrona.Poltrona', on_delete=models.CASCADE, db_default=1)    
    status = models.IntegerField(db_default=1, default=1) # 0- Apagado 1 - Ativo
    forma_pagamento = models.CharField(max_length=50, default='Pendente')  # Ex: Cartão de crédito, Dinheiro, Pix
    id_pagamento = models.CharField(max_length=100, default='Pendente')  # ID do pagamento, se aplicável
    grupo = models.CharField(max_length=12,editable=False)  # Grupo do pedido
    date_created = models.DateField(auto_now_add=True)

