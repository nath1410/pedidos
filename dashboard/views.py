# -*- coding: utf-8 -*-
from django.shortcuts import render
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.
def index(request):
    return render(request, 'index.html')
