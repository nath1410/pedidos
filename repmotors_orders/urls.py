# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
#from django.contrib.staticfiles.url import staticfiles_urlpatterns
from django.contrib import admin
import product.views
import logging

logger = logging.getLogger(__name__)

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:

    url(r'^$', 'dashboard.views.index',),
    url(r'^index/', 'dashboard.views.index',),
    url(r'^dashboard/', 'product.views.product',),
    url(r'^produtos/', 'product.views.product', name='produtos'),
    url(r'^produtoForm/(?P<pk>[0-9]+)/?$', product.views.ItemUpdateView.as_view(), name='produtoForm'),
    url(r'^clientes/', 'people.views.customers'),
    url(r'^vendedores/', 'people.views.vendors'),
    url(r'^pedidos/', 'order.views.pedidos'),
    url(r'^admin/', include(admin.site.urls)),
    )

