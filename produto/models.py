# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Produto(models.Model):

        idProduto = models.AutoField(primary_key = True)
        deProduto = models.CharField(max_length = 200)
        idTamanho = models.ForeignKey('Tamanho')
        deCor = models.CharField(max_length = 20)
        idUnidade = models.ForeignKey('Unidade')

class Unidade(models.Model):

        idUnidade  = models.CharField(primary_key = True, max_length = 3)
        deUnidade = models.CharField(max_length = 20)
        idUnidadeConversao = models.ForeignKey('self')
        nuTaxaConversao = models.FloatField()

class Tamanho(models.Model):

        idTamanho = models.CharField(primary_key = True, max_length = 3)
        deTamanho = models.CharField(max_length = 20)
