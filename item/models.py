# -*- coding: utf-8 -*-
from django.db import models
from pedido.models import Pedido
from produto.models import Produto, Unidade


# Create your models here.
class Item(models.Model):

        idPedido = models.ForeignKey(pedido.models.Pedido, primary_key=True)
        idItem = models.AutoField(primary_key=True)
        idProduto = models.ForeignKey(produto.models.Produto)
        idUnidade = models.ForeignKey(produto.models.Unidade)
        nuQuantidade = models.IntegerField()
        deObservacao = models.CharField(max_length=1000)
