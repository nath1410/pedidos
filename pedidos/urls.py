# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
#from django.contrib.staticfiles.url import staticfiles_urlpatterns
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:

    url(r'^$', 'dashboard.views.index',),
    url(r'^index/', 'dashboard.views.index',),
    url(r'^dashboard/', 'produto.views.produto',),
    url(r'^produtos/', 'produto.views.produto'),
    url(r'^produtosForm/([0-9]{1})/$', 'produto.views.produto', name='news-year-archive'),
    url(r'^clientes/', 'pessoa.views.clientes'),
    url(r'^vendedores/', 'pessoa.views.vendedores'),
    url(r'^pedidos/', 'pedido.views.pedidos'),
    url(r'^admin/', include(admin.site.urls)),
)

