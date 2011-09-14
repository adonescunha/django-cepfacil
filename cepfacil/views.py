# -*- coding: utf-8 -*-

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

def service(self, cep, format):
    if not getattr(settings, 'CEPFACIL_CODE', ''):
        raise ImproperlyConfigured, 'Missing CEPFACIL_CODE setting.'
