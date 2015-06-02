# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from inicio.models import Pais
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
          return render(request, 'index.html')



def index2(request):
           return render(request, 'index2.html')

