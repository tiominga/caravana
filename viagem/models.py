from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from datetime import date


# Create your models here.
class Viagem(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField()
    hora_partida = models.TimeField()
    hora_chegada = models.TimeField()
    local_partida = models.CharField(max_length=200,default='')
    origem = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(db_default='')
    obs = models.TextField(db_default='')
    cod_usuario = models.ForeignKey(User, on_delete=models.CASCADE,db_default=1)  # Relacionando com o modelo User
    acentos_andar1d = models.IntegerField(db_default=1)
    acentos_andar1e = models.IntegerField(db_default=1)
    acentos_andar2d = models.IntegerField(db_default=1)
    acentos_andar2e = models.IntegerField(db_default=1)
    date_add = models.DateTimeField(auto_now_add=True)

    def clean(self):
       if self.nome =='':
          raise ValidationError('O nome da viagem precisa ser preenchido')

       if not self.data:
           raise ValidationError('A data da viagem precisa ser preenchida')
       
       if not self.hora_partida:
           raise ValidationError('A hora de partida precisa ser preenchida')
       
       if not self.hora_chegada:
           raise ValidationError('A hora de chegada precisa ser preenchida')
       
       if self.origem == '':
           raise ValidationError('A origem precisa ser preenchida')
       
       if self.destino == '':
           raise ValidationError('O destino precisa ser preenchido') 
       
       if self.local_partida == '':
              raise ValidationError('O local de partida precisa ser preenchido')

       if self.preco is None or self.preco < 0:
           raise ValidationError('O preço da viagem precisa ser preenchido e maior ou igual a zero')
       


