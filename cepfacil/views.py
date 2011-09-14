# -*- coding: utf-8 -*-

import urllib
import urllib2
import urlparse
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponse
from django.utils import simplejson

MIMETYPES = {
    'xml': 'text/xml',
    'json': 'text/javascript'
}

FORMAT_ALIASES = {
    'xml': 'xml',
    'json': 'texto'
}

def service(self, cep, format):
    code = getattr(settings, 'CEPFACIL_CODE', '')

    if not code:
        raise ImproperlyConfigured, "You haven't set the CEPFACIL_CODE setting yet."

    response = urllib2.urlopen('http://www.cepfacil.com.br/service?%s' %\
        urllib.urlencode({'filiacao': code, 'cep': cep, 'formato': FORMAT_ALIASES[format]})).read()

    if format == 'json':
        response = urlparse.parse_qs(response)

        return HttpResponse(simplejson.dumps(response, ensure_ascii=False),
            mimetype='text/javascript')

    return HttpResponse(response, mimetype=MIMETYPES[format])
