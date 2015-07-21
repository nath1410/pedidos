# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.generic import UpdateView
from produto.forms import ProdutoForm
from produto.models import Produto


def produto(request):
    produtos = Produto.objects.all()

    return render(request, 'produto.html',
        {
            'produtos': produtos,
        }
    )

class ItemUpdateView(UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produtoForm.html'

    def dispatch(self, *args, **kwargs):
        self.item_id = kwargs['pk']
        return super(ItemUpdateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.save()
        produto = Produto.objects.get(id=self.idProduto)
        #return HttpResponse(render_to_string('produto'))
        return HttpResponse(render_to_string('produtoFormSuccess.html', {'produto': produto}))
