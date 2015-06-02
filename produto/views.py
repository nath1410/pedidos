# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from produto.models import Produto


def produto(request):
    produtos = Produto.objects.all()

    return render(request, 'produto.html',
        {
            'produtos': produtos,
        }
    )