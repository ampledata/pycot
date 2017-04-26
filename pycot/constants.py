#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Python Cursor on Target Module Constants."""

import logging
import os
import sys

__author__ = 'Greg Albrecht <oss@undef.net>'
__copyright__ = 'Copyright 2017 Orion Labs, Inc.'
__license__ = 'Apache License, Version 2.0'


if bool(os.environ.get('DEBUG_PYCOT')) or bool(os.environ.get('DEBUG_ALL')):
    LOG_LEVEL = logging.DEBUG
else:
    LOG_LEVEL = logging.INFO

LOG_FORMAT = logging.Formatter(
    ('%(asctime)s pycot %(levelname)s %(name)s.%(funcName)s:%(lineno)d - '
     '%(message)s'))

if sys.version_info.major == 2:
    BaseStrType = basestring
else:
    BaseStrType = str
