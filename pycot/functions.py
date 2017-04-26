#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Python Cursor on Target Module Function Definitions."""

import pycot

__author__ = 'Greg Albrecht <oss@undef.net>'
__copyright__ = 'Copyright 2017 Orion Labs, Inc.'
__license__ = 'Apache License, Version 2.0'


def parse_event_type(event_type):
    if event_type.startswith('a'):
        return pycot.AtomEventType(event_type)

    elif event_type.startswith('b'):
        return pycot.DataEventType(event_type)

        describes = 'Data'
        type_fields = ['describes', 'dimension']

    elif event_type.startswith('c'):
        describes = 'Capability'

    elif event_type.startswith('r'):
        describes = 'Reservation'

    elif event_type.startswith('t'):
        describes = 'Tasking'
