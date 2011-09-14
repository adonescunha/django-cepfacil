# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='django-cepfacil',
    version='0.0.1',
    description='A Django app that provides a wrapper to CEP Fácil web service.',
    author='Adones Cunha',
    author_email='hi@adonescunha.com',
    url='http://github.com/adonescunha/django-cepfacil/',
    packages=[
        'cepfacil'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        'Topic :: Utilities'
    ],
    install_requires=[
       'django'
    ]
)
