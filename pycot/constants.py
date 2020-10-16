#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Python Cursor on Target Module Constants."""

import logging
import os

__author__ = 'Greg Albrecht W2GMD <oss@undef.net>'
__copyright__ = 'Copyright 2020 Orion Labs, Inc.'
__license__ = 'Apache License, Version 2.0'


if bool(os.environ.get('DEBUG')):
    LOG_LEVEL = logging.DEBUG
    LOG_FORMAT = logging.Formatter(
        ('%(asctime)s pycot %(levelname)s %(name)s.%(funcName)s:%(lineno)d - '
         '%(message)s'))
    logging.debug('pycot Debugging Enabled via DEBUG Environment Variable.')
else:
    LOG_LEVEL = logging.INFO
    LOG_FORMAT = logging.Formatter(
        ('%(asctime)s pycot %(levelname)s - %(message)s'))


DEFAULT_COT_PORT: int = 8087
