# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
#from django.contrib.staticfiles.url import staticfiles_urlpatterns
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:

    url(r'^$', 'dashboard.views.index',),
    url(r'^index2/', 'dashboard.views.index2',),
    url(r'^produto/', 'produto.views.produto'),
    url(r'^admin/', include(admin.site.urls)),
)

