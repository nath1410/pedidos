# -*- coding: utf-8 -*-
import logging

from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.generic import UpdateView

from .forms import ProdutoForm
from .models import Product

logger = logging.getLogger(__name__)


def product(request):
    products = Product.objects.all()

    logger.error('product(request)')
    return render(request, 'product.html',
        {
            'products': products,
        }
    )


class ItemUpdateView(UpdateView):

    logger.error('ItemUpdateView')
    model = Product
    form_class = ProdutoForm
    template_name = 'productForm.html'

    def dispatch(self, *args, **kwargs):
        logger.error('dispatch')
        self.idProduto = kwargs['pk']
        return super(ItemUpdateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        logger.error('form_valid')
        form.save()
        produto = Product.objects.get(id=self.idProduto)
        return HttpResponse(render_to_string('productFormSuccess.html',
            {'product': produto}))

    def get_context_data(self, **kwargs):
        logger.error('get_context_data')
        context = super(ItemUpdateView, self).get_context_data(**kwargs)
        return context
