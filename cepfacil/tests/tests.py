# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.core.exceptions import ImproperlyConfigured

class ServiceTestCase(TestCase):
    """
    Test cepfacil.views.service
    """

    def test_request_without_CEPFACIL_CODE_set(self):
        self.assertRaises(
            ImproperlyConfigured,
            self.client.get,
            reverse('cepfacil_service', args=['51130000', 'json'])
        )
