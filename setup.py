#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Setup for the Python Cursor on Target Module.

:author: Greg Albrecht <oss@undef.net>
:copyright: Copyright 2017 Orion Labs, Inc.
:license: Apache License, Version 2.0
:source: <https://github.com/OnBeep/pycot>
"""

import os
import setuptools
import sys

__title__ = 'pycot'
__version__ = '0.0.1'
__author__ = 'Greg Albrecht <oss@undef.net>'
__copyright__ = 'Copyright 2017 Orion Labs, Inc.'
__license__ = 'Apache License, Version 2.0'


def publish():
    """Function for publishing package to pypi."""
    if sys.argv[-1] == 'publish':
        os.system('python setup.py sdist')
        os.system('twine upload dist/*')
        sys.exit()


publish()


setuptools.setup(
    name=__title__,
    version=__version__,
    description='Python Cursor on Target Module.',
    author='Greg Albrecht',
    author_email='oss@undef.net',
    packages=['pycot'],
    package_data={'': ['LICENSE']},
    package_dir={'pycot': 'pycot'},
    license=open('LICENSE').read(),
    long_description=open('README.rst').read(),
    url='https://github.com/OnBeep/pycot',
    zip_safe=False,
    include_package_data=True,
    setup_requires=[
      'coverage >= 3.7.1',
      'httpretty >= 0.8.10',
      'nose >= 1.3.7'
    ],
    install_requires=[
        'dexml2>=0.5.3'
    ],
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: Apache Software License'
    ],
    keywords=[
        'Cursor on Target'
    ]
)
