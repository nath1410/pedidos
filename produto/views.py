# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.generic import UpdateView
from .forms import ProdutoForm
from .models import Produto
import logging

logger = logging.getLogger(__name__)


def produto(request):
    produtos = Produto.objects.all()

    logger.error('produto(request)')
    return render(request, 'produto.html',
        {
            'produtos': produtos,
        }
    )


class ItemUpdateView(UpdateView):

    logger.error('ItemUpdateView')
    model = Produto
    form_class = ProdutoForm
    template_name = 'produtoForm.html'

    def dispatch(self, *args, **kwargs):
        logger.error('dispatch')
        self.idProduto = kwargs['pk']
        return super(ItemUpdateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        logger.error('form_valid')
        form.save()
        produto = Produto.objects.get(id=self.idProduto)
        return HttpResponse(render_to_string('produtoFormSuccess.html', 
            {'produto': produto}))

    def get_context_data(self, **kwargs):
        logger.error('get_context_data')
        context = super(ItemUpdateView, self).get_context_data(**kwargs)
        return context
