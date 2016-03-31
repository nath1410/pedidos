# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
# from django.contrib.staticfiles.url import staticfiles_urlpatterns
from django.contrib import admin
import product.views
import people.views
import logging

logger = logging.getLogger(__name__)

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:

                       url(r'^$', 'dashboard.views.index', ),
                       url(r'^index/', 'dashboard.views.index', ),
                       url(r'^dashboard/', 'product.views.product', ),
                       url(r'^produtos/', 'product.views.product', name='produtos'),
                       # url(r'^produtoForm/(?P<id>[0-9]+)/', product.views.ItemUpdateView.as_view(), name='produtoForm'),
                       # url(r'^products_form/(?P<pk>[0-9]+)/', 'product.views.products_form', name='products_form'),
                       url(r'^products_form/(?P<pk>\d+)/$', product.views.products_edit, {}, 'products_form'),
                       url(r'^clientes/', 'people.views.customers'),
                       # url(r'^clientesForm/(?P<id>[0-9]+)/', people.views.ItemUpdateView.as_view(), name='clientesForm'),
                       # url(r'^customers_form/(?P<pk>[0-9]+)/', 'people.views.customers_form', name='customers_form'),
                       url(r'^customers_form/(?P<pk>[0-9]+)/', people.views.customers_edit, name='customers_form'),
                       url(r'^vendedores/', 'people.views.vendors'),
                       url(r'^orders/', 'order.views.orders'),
                       url(r'^admin/', include(admin.site.urls)),
                       )
