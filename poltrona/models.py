from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from datetime import date

class Poltrona(models.Model):   
    nome = models.CharField(max_length=100,blank=True, null=True)
    cod_passageiro = models.IntegerField(blank=True, null=True)
    cod_viagem = models.IntegerField(blank=True, null=True)
    cod_pagamento = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(db_default=1,default=1)
    date_created = models.DateField(auto_now_add=True)

    def clean(self):
        if self.cod_vaigem == '':
            raise ValidationError('O código da viagem precisa ser informado.')