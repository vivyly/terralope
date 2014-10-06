# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import terralope
version = terralope.__version__

setup(
    name='terralope',
    version=version,
    author='',
    author_email='vivyly9@gmail.com',
    packages=[
        'terralope',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.5',
    ],
    zip_safe=False,
    scripts=['terralope/manage.py'],
)