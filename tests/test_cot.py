#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Python Cursor on Target Module Tests."""

from .context import pycot

from . import constants

__author__ = 'Greg Albrecht <oss@undef.net>'
__copyright__ = 'Copyright 2017 Orion Labs, Inc.'
__license__ = 'Apache License, Version 2.0'


_keys = ['version', 'event_type', 'access', 'qos', 'opex', 'uid', 'time', 'start', 'stale', 'how', 'point', 'detail']

basic = """<?xml version='1.0' standalone='yes'?>
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

my_point = pycot.Point()
my_point.lat = '37.76'
my_point.lon = '-122.4975'
my_point.ce = '45.3'
my_point.le = '99.5'
my_point.hae = '-42.6'


e = pycot.Event()
e.version = '0.1'
e.type = 'a-h-G-p-i'
e.uid = '123'
e.time = '123'
e.start = '123'
e.stale = '123'
e.how = 'h-e'
e.point = my_point


print "--- Generated ---"
print e
print e.render()

#for k in _keys:
#    print getattr(e, k)

#print dir(e.event_type)
#print e.event_type.describes

#with open('test.xml', 'w') as ofd:
#    print e.export(ofd, 1)

print "--- Parsed ---"
p = pycot.Event
x = p.parse(basic)
print x.render()
