# -*- coding: utf-8 -*-
from produto.models import Produto
from django import forms

class ProdutoForm(forms.Form):

    def __init__(self, instance, *args, **kwargs):
      super(ProdutoForm, self).__init__(*args, **kwargs)
      #deProduto = forms.CharField(max_length = 200)
      #deCor = forms.CharField(max_length = 20)
      #self.fields['deProduto'].widget.attrs['class'] = 'calendar'

    class Meta:
      model = Produto
      fields = '__all__'