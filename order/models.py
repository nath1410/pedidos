# -*- coding: utf-8 -*-
from django.db import models

from people.models import Customer, Vendor


# Create your models here.
class Order(models.Model):

        id = models.AutoField(primary_key=True)
        customer = models.ForeignKey(Customer)
        vendor = models.ForeignKey(Vendor)
