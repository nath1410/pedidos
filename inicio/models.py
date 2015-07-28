# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.
class Usuario(models.Model):

        cdUsuario = models.CharField(max_length=30)
        deUsuario = models.CharField(max_length=100)
        deSenha = models.CharField(max_length=10)
        flAtivo = models.BooleanField()

        def __unicode__(self):
            return self.deUsuario


class Cidade(models.Model):

        idCidade = models.AutoField(primary_key=True)
        idUf = models.ForeignKey('UF')
        deCidade = models.CharField(max_length=50)
        IBGE = models.IntegerField()

        def __unicode__(self):
            return self.deCidade


class UF(models.Model):

        idUf = models.CharField(primary_key=True, max_length=2)
        deUf = models.CharField(max_length=30)
        idPais = models.ForeignKey('Pais')
        IBGE = models.IntegerField()

        def __unicode__(self):
            return self.deUf


class Pais(models.Model):

        idPais = models.AutoField(primary_key=True)
        dePais = models.CharField(max_length=50)

        def __unicode__(self):
            return self.dePais
