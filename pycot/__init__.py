#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python Cursor on Target Module.

"""
Python Cursor on Target Module.
~~~~


:author: Greg Albrecht <oss@undef.net>
:copyright: Copyright 2017 Orion Labs, Inc.
:license: Apache License, Version 2.0
:source: <https://github.com/OnBeep/pycot>

"""

from .constants import BaseStrType  # NOQA

from .utils import cast, showIndent  # NOQA

from .functions import parse_event_type  # NOQA

from .classes import Event, Point, Detail  # EventType, AtomEventType, DataEventType  # NOQA

__author__ = 'Greg Albrecht <oss@undef.net>'
__copyright__ = 'Copyright 2017 Orion Labs, Inc.'
__license__ = 'Apache License, Version 2.0'
