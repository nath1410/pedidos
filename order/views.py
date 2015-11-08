# -*- coding: utf-8 -*-
from django.shortcuts import render

from .models import Order


def pedidos(request):
    pedidos = Order.objects.all()

    return render(request, 'order.html',
        {
            'repmotors_orders': pedidos,
        }
    )
