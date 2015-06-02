# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from inicio.models import Pais


# Create your views here.
def index(request):
    pais = Pais.objects.all()

    return render(request, 'index.html',
        {
            'pais': pais,
        }
    )

def index2(request):
           return render(request, 'index2.html')

