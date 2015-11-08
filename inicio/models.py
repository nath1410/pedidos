# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.
class User(models.Model):

        id = models.CharField(primary_key=True, max_length=30)
        name = models.CharField(max_length=100)
        password = models.CharField(max_length=10)
        active = models.BooleanField(default=True)

        def __unicode__(self):
            return self.name


class City(models.Model):

        id = models.AutoField(primary_key=True)
        state = models.ForeignKey('State')
        nome = models.CharField(max_length=50)
        ibge = models.IntegerField()

        def __unicode__(self):
            return self.nome


class State(models.Model):

        id = models.CharField(primary_key=True, max_length=2)
        name = models.CharField(max_length=30)
        contry = models.ForeignKey('Contry')
        ibge = models.IntegerField()

        def __unicode__(self):
            return self.name


class Contry(models.Model):

        id = models.AutoField(primary_key=True)
        name = models.CharField(max_length=50)

        def __unicode__(self):
            return self.name
