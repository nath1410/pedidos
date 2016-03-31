# -*- coding: utf-8 -*-
from django.shortcuts import render

from .models import Order


def orders(request):
    orders = Order.objects.all()

    return render(request, 'order.html', {'orders': orders})
