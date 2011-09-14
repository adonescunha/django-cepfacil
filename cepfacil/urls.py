# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('cepfacil.views',
    url(r'^(?P<cep>\d{8}).(?P<format>\w+)$', 'service', name='cepfacil_service')
)
