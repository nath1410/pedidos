# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from pessoa.models import Cliente
from pessoa.models import Vendedor


def clientes(request):
    clientes = Cliente.objects.all()

    return render(request, 'clientes.html',
        {
            'clientes': clientes,
        }
    )

def vendedores(request):
    vendedores = Vendedor.objects.all()

    return render(request, 'vendedores.html',
        {
            'vendedores': vendedores,
        }
    )