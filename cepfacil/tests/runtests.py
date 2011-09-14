#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
from django.conf import settings

TEST_ROOT = os.path.dirname(os.path.abspath(__file__))

if not settings.configured:
    settings.configure(
        TEST_ROOT=TEST_ROOT,
        DEBUG=True,
        DATABASE_ENGINE='sqlite3',
        DATABASE_NAME=os.path.join(TEST_ROOT, 'database.db'),
        ROOT_URLCONF='cepfacil.tests.urls',
        INSTALLED_APPS=(
            'tests',
            'cepfacil',
        ),
    )

from django.test.simple import run_tests

def runtests(*args):
    if not args:
        args = ['tests']

    sys.path.insert(0, os.path.dirname(TEST_ROOT))
    sys.path.insert(0, os.path.dirname(os.path.dirname(TEST_ROOT)))
    failures = run_tests(args, verbosity=1, interactive=True)
    sys.exit(failures)

if __name__ == '__main__':
    runtests(*sys.argv[1:])
