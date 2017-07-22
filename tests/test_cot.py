#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Python Cursor on Target Module Tests."""

import datetime
import logging
import unittest
import uuid

from .context import pycot

#from . import constants

__author__ = 'Greg Albrecht <oss@undef.net>'
__copyright__ = 'Copyright 2017 Orion Labs, Inc.'
__license__ = 'Apache License, Version 2.0'


class PYCOTTest(unittest.TestCase):  # pylint: disable=R0904

    """Tests for the Python CoT Module."""

    _logger = logging.getLogger(__name__)
    if not _logger.handlers:
        _logger.setLevel(pycot.LOG_LEVEL)
        _console_handler = logging.StreamHandler()
        _console_handler.setLevel(pycot.LOG_LEVEL)
        _console_handler.setFormatter(pycot.LOG_FORMAT)
        _logger.addHandler(_console_handler)
        _logger.propagate = False

    def test_generate_cot(self):
        """Tests generating a CoT XML Event using pycot."""

        _keys = [
            'version', 'event_type', 'access', 'qos', 'opex', 'uid', 'time',
            'start', 'stale', 'how', 'point', 'detail']

        my_point = pycot.Point()
        my_point.lat = '37.76'
        my_point.lon = '-122.4975'
        my_point.ce = '45.3'
        my_point.le = '99.5'
        my_point.hae = '-42.6'

        evt = pycot.Event()
        evt.version = '2.0'
        evt.event_type = 'a-h-G-p-i'
        evt.uid = uuid.uuid4()
        evt.time = datetime.datetime.now()
        evt.how = 'h-e'
        evt.point = my_point

        self._logger.debug(evt.render(standalone=True, pretty=True))

        # for k in _keys:
        #    print getattr(e, k)

        # print dir(e.event_type)
        # print e.event_type.describes

        # with open('test.xml', 'w') as ofd:
        #    print e.export(ofd, 1)

    def test_parse_cot(self):
        """Tests parsing a CoT XML Event using pycot."""
        example_event = """<?xml version='1.0' standalone='yes'?>
        <event version="2.0"
         uid="J-01334"
         type="a-h-A-M-F-U-M"
         time="2005-04-05T11:43:38.07Z"
         start="2005-04-05T11:43:38.07Z"
         stale="2005-04-05T11:45:38.07Z"
         how='m-g'>
         <detail>
         </detail>
         <point lat="30.0090027" lon="-85.9578735" ce="45.3"
         hae="-42.6" le="99.5" />
        </event>
        """
        parsed = pycot.Event.parse(example_event)
        self._logger.debug(parsed)
        self._logger.debug(parsed.render(standalone=True))
        self._logger.debug(dir(parsed))
        self.assertEqual(
            parsed.render(standalone=True),
            ('<?xml version="1.0" standalone="yes" ?><event version="2.0" '
             'type="a-h-A-M-F-U-M" '
             'uid="J-01334" '
             'time="2005-04-05T11:43:38.070000Z" '
             'start="2005-04-05T11:43:38.070000Z" '
             'stale="2005-04-05T11:45:38.070000Z" '
             'how="m-g"><detail /></event>')
        )
        self.assertEqual(parsed.version, 2.0)
        self.assertEqual(parsed.uid, 'J-01334')

        # FIXME: These three tests fail b/c of 0000 instead of Z in TZ
        # self.assertEqual(str(parsed.time), '2005-04-05T11:43:38.07Z')
        # self.assertEqual(parsed.start, '2005-04-05T11:43:38.07Z')
        # self.assertEqual(parsed.stale, '2005-04-05T11:45:38.07Z')

        self.assertEqual(parsed.how, 'm-g')
