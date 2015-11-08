# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.
class Product(models.Model):

        id = models.AutoField(primary_key=True)
        name = models.CharField(max_length=200)
        size = models.ForeignKey('Size')
        color = models.CharField(max_length=20)
        unit = models.ForeignKey('Unit')

        def __unicode__(self):
                return self.id


class Unit(models.Model):

        id = models.CharField(primary_key=True, max_length=3)
        name = models.CharField(max_length=20)
        conversion_unit = models.ForeignKey('self')
        conversion_tax = models.FloatField()

        def __unicode__(self):
                return self.id


class Size(models.Model):

        id = models.CharField(primary_key=True, max_length=3)
        name = models.CharField(max_length=20)

        def __unicode__(self):
                return self.id
