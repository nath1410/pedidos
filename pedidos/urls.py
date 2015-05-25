from django.conf.urls import patterns, include, url
#from django.contrib.staticfiles.url import staticfiles_urlpatterns
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:

    url(r'^$', 'dashboard.views.index2', name='dashboard_index_2'),
    url(r'^index/', 'dashboard.views.index'),
    url(r'^index2/', 'dashboard.views.index2', name='dashboard_index2'),
    url(r'^admin/', include(admin.site.urls)),
)

