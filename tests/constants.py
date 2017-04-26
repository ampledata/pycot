#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Python Cursor on Target Module Test Constants."""

__author__ = 'Greg Albrecht <oss@undef.net>'
__copyright__ = 'Copyright 2017 Orion Labs, Inc.'
__license__ = 'Apache License, Version 2.0'


PANGRAM = 'the quick brown fox jumps over the lazy dog'
ALPHABET = PANGRAM.replace(' ', '')

NUMBERS = ''.join([str(x) for x in range(0, 10)])
POSITIVE_NUMBERS = NUMBERS[1:]
ALPHANUM = ''.join([ALPHABET, NUMBERS])
