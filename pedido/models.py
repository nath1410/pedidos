# -*- coding: utf-8 -*-
from django.db import models
import pessoa.models
import produto.models

# Create your models here.
class Pedido(models.Model):

        idPedido = models.AutoField(primary_key = True)
        idCliente = models.ForeignKey(pessoa.models.Cliente)
        idProduto = models.ForeignKey(produto.models.Produto)
        idUnidade = models.ForeignKey(produto.models.Unidade)
        idVendedor = models.ForeignKey(pessoa.models.Vendedor)
        nuQuantidade = models.IntegerField()
