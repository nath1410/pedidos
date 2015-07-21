# -*- coding: utf-8 -*-
from django import forms

class ProdutoForm(forms.Form):
    #idProduto = forms.AutoField(primary_key = True)
    deProduto = forms.CharField(max_length = 200)
    #idTamanho = forms.ForeignKey('Tamanho')
    deCor = forms.CharField(max_length = 20)
    #idUnidade = forms.ForeignKey('Unidade')