# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.
class Item(models.Model):

        id = models.AutoField(primary_key=True)
        order = models.ForeignKey(order.models.Order, primary_key=True)
        product = models.ForeignKey(product.models.Product)
        unit = models.ForeignKey(product.models.Unit)
        quantity = models.IntegerField()
        observation = models.CharField(max_length=1000)
