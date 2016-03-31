# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ProductForm
from .models import Product


def product(request):
    products = Product.objects.all()

    return render(request, 'product.html', {'products': products})


def products_form(request, pk):
    products = Product.objects.get(id=1)
    form = ProductForm(instance=products)

    return render(request, 'product_form.html', {'products': form})


def products_edit(request, pk=None):
    if id:
        product = Product.objects.get(id=pk)
    else:
        product = Product(id=1)

    if request.POST:
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()

            # If the save was successful, redirect to another page
            redirect_url = reverse('produtos')
            return HttpResponseRedirect(redirect_url)
    else:
        form = ProductForm(instance=product)

    return render(request, 'product_form.html', {'form': form, 'product': product})

