from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from datetime import date

class passageiro(models.Model):    
    nome = models.CharField(max_length=150)
    rua = models.CharField(max_length=150)
    numero = models.IntegerField()
    cep = models.CharField(max_length=10)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(choices=[('AC', 'AC'), ('AL', 'AL'), ('AP', 'AP'), ('AM', 'AM'), ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'), ('GO', 'GO'), ('MA', 'MA'), ('MG', 'MG'), ('MS', 'MS'), ('MT', 'MT'), ('PA', 'PA'), ('PB', 'PB'), ('PE', 'PE'), ('PI', 'PI'), ('PR', 'PR'), ('RJ', 'RJ'), ('RN', 'RN'), ('RO', 'RO'), ('RR', 'RR'), ('RS', 'RS'), ('SC', 'SC'), ('SE', 'SE'), ('SP', 'SP'), ('TO', 'TO')], max_length=255)
    celular = models.CharField(max_length=15, null=True, blank=True)
    status = models.IntegerField(default=1, db_default=1)
    obs = models.CharField(max_length=255)
    cod_usuario = models.ForeignKey(User,on_delete=models.PROTECT,related_name='viagens',null=True,blank=True)    
    date_created = models.DateField(auto_now_add=True)

    def clean(self):
        if self.nome =='':
            raise ValidationError('Nome não pode ser em branco.')

    def clean(self):
        if self.rua =='':
            raise ValidationError('Rua não pode ser em branco.')
        
    def clean(self):
        if self.cep =='':
            raise ValidationError('Cep não pode ser em branco.')

    def clean(self):
        if self.cidade =='':
            raise ValidationError('Cidade não pode ser em branco.')

    def clean(self):
        if self.estado =='':
            raise ValidationError('Estado não pode ser em branco.')        


    

