#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Python Cursor on Target Module Function Definitions."""

import pycot

__author__ = 'Greg Albrecht <oss@undef.net>'
__copyright__ = 'Copyright 2020 Orion Labs, Inc.'
__license__ = 'Apache License, Version 2.0'


def parse_event_type(event_type: str) -> pycot.EventType:
    """Parses CoT Event Types from CoT Events."""
    if event_type.startswith('a'):
        return pycot.AtomEventType(event_type)
    elif event_type.startswith('b'):
        return pycot.DataEventType(event_type)
    elif event_type.startswith('c'):
        describes = 'Capability'
        raise pycot.UnsupportedEvent(f'Unsupported Event type: {describes}')
    elif event_type.startswith('r'):
        describes = 'Reservation'
        raise pycot.UnsupportedEvent(f'Unsupported Event type: {describes}')
    elif event_type.startswith('t'):
        describes = 'Tasking'
        raise pycot.UnsupportedEvent(f'Unsupported Event type: {describes}')
    else:
        raise pycot.UnsupportedEvent(f'Unknown Event Type: {event_type}')
