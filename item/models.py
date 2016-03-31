# -*- coding: utf-8 -*-
from django.db import models

from order.models import Order
from product.models import Product


# Create your models here.
class Item(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()
    observation = models.CharField(max_length=1000)
