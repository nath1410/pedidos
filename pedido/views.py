# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from pedido.models import Pedido


def pedidos(request):
    pedidos = Pedido.objects.all()

    return render(request, 'pedidos.html',
        {
            'pedidos': pedidos,
        }
    )