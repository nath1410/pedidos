# -*- coding: utf-8 -*-
from django.db import models
import pessoa.models

# Create your models here.
class Pedido(models.Model):

        idPedido = models.AutoField(primary_key = True)
        idCliente = models.ForeignKey(pessoa.models.Cliente)
        idVendedor = models.ForeignKey(pessoa.models.Vendedor)
