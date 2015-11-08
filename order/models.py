# -*- coding: utf-8 -*-
from django.db import models
#from people.models import Customer, Vendor
import people.models


# Create your models here.
class Order(models.Model):

        id = models.AutoField(primary_key=True)
        client = models.ForeignKey(people.models.Customer)
        vendor = models.ForeignKey(people.models.Vendor)
