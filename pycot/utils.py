#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Python Cursor on Target Module Utility Function Definitions."""

import re

__author__ = 'Greg Albrecht W2GMD <oss@undef.net>'
__copyright__ = 'Copyright 2020 Orion Labs, Inc.'
__license__ = 'Apache License, Version 2.0'


def cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)


def parse_qos(qos):
    matches = re.search(
        r'(?<priority>\d)-(?<overtaking>\w)-(?<assurance>\w)', qos)
    return matches


def show_indent(outfile, level, pretty_print=True):
    if pretty_print:
        for _ in range(level):
            outfile.write('    ')
