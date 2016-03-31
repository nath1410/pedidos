# -*- coding: utf-8 -*-
from django.db import models

from inicio.models import City


# Create your models here.
class People(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    rg = models.CharField(max_length=10)
    cnpjf = models.CharField(max_length=14)
    ie = models.CharField(max_length=9)
    phone = models.CharField(max_length=14)
    mail = models.EmailField(max_length=80)
    creation_date = models.DateTimeField(auto_now=True)
    birthday_date = models.DateField(auto_now=False)
    address = models.ForeignKey('Address')
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name


class Customer(People):
    max_discount = models.FloatField()


class Vendor(People):
    commission = models.FloatField()


class Address(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    complement = models.CharField(max_length=150)
    number = models.IntegerField()
    cep = models.CharField(max_length=8)
    district = models.CharField(max_length=30)
    city = models.ForeignKey(City)
