# -*- coding: utf-8 -*-
import logging
from django import forms
from .models import Produto

logger = logging.getLogger(__name__)


class ProdutoForm(forms.Form):

    def __init__(self, instance, *args, **kwargs):
        logger.error('form __init__')
        super(ProdutoForm, self).__init__(*args, **kwargs)
        logger.error('form __init__ 1')
        deProduto = forms.CharField(label='DescricaoProduto', max_length=200)
        deCor = forms.CharField(max_length = 20)
        #self.fields['deProduto'].widget.attrs['class'] = 'calendar'

    class Meta:
        logger.error('form Meta')
        model = Produto
        fields = '__all__'