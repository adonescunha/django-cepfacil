# -*- coding: utf-8 -*-

from django.test import TestCase
from django.conf import settings
from django.core.urlresolvers import reverse
from django.core.exceptions import ImproperlyConfigured

class ServiceTestCase(TestCase):
    """
    Test cepfacil.views.service
    """

    def test_request_without_CEPFACIL_CODE_set(self):
        """CEPFACIL_CODE must be set."""

        cepfacil_code_backup = settings.CEPFACIL_CODE
        settings.CEPFACIL_CODE = None

        self.assertRaises(
            ImproperlyConfigured,
            self.client.get,
            reverse('cepfacil_service', args=['51130000', 'json'])
        )

        settings.CEPFACIL_CODE = cepfacil_code_backup

    def test_json_request(self):
        response = self.client.get(reverse('cepfacil_service',
            args=['51130000', 'json']))

        self.assertContains(response, 'Boa Viagem')
