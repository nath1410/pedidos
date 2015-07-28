# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import Pedido


def pedidos(request):
    pedidos = Pedido.objects.all()

    return render(request, 'pedidos.html',
        {
            'pedidos': pedidos,
        }
    )
