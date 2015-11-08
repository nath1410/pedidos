# -*- coding: utf-8 -*-
from django.shortcuts import render

from .models import Customer
from .models import Vendor


def customers(request):
    customers = Customer.objects.all()

    return render(request, 'customer.html',
        {
            'customers': customers,
        }
    )


def vendors(request):
    vendors = Vendor.objects.all()

    return render(request, 'vendor.html',
        {
            'vendors': vendors,
        }
    )
