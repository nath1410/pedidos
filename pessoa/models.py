# -*- coding: utf-8 -*-
from django.db import models
from inicio.models import Cidade


# Create your models here.
class Pessoa(models.Model):

        idPessoa = models.AutoField(primary_key=True)
        dePessoa = models.CharField(max_length=100)
        RG = models.CharField(max_length=10)
        CNPJF = models.CharField(max_length=14)
        InscEstadual = models.CharField(max_length=9)
        nuTelefone = models.CharField(max_length=11)
        email = models.EmailField(max_length=80)
        dtCadastro = models.DateTimeField(auto_now=True)
        dtAniversario = models.DateField(auto_now=False)
        idEndereco = models.ForeignKey('Endereco')
        flAtivo = models.BooleanField()

        class Meta:
            abstract = True

        def __unicode__(self):
            return self.dePessoa


class Cliente(Pessoa):

        nuDescontoMaximo = models.FloatField()


class Vendedor(Pessoa):

        nuComissao = models.FloatField()



class Endereco(models.Model):
        RUA = 'R'
        TRAVESSA = 'T'
        AVENIDA = 'A'
        RODOVIA = 'BR'
        SERVIDAO = 'S'

        LOGADOURO = (
            (RUA, 'Rua'),
            (TRAVESSA, 'Travessa'),
            (AVENIDA, 'Avenida'),
            (RODOVIA, 'Rodovia'),
            (SERVIDAO, 'Servidão'),
        )

        idEndereco = models.AutoField(primary_key=True)
        cdLogadouro = models.CharField(max_length=2, 
            choices=LOGADOURO, default=RUA)
        deRua = models.CharField(max_length=100)
        deComplemento = models.CharField(max_length=150)
        nuNumero = models.IntegerField()
        nuCep = models.CharField(max_length=8)
        deBairro = models.CharField(max_length=30)
        idCidade = models.ForeignKey(inicio.models.Cidade)
