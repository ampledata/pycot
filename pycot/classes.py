#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Python Cursor on Target Module Class Definitions."""

import dexml2

__author__ = 'Greg Albrecht <oss@undef.net>'
__copyright__ = 'Copyright 2017 Orion Labs, Inc.'
__license__ = 'Apache License, Version 2.0'


class Point(dexml2.Model):
    class meta:
        tagname = 'point'
    lat = dexml2.fields.Float()
    lon = dexml2.fields.Float()
    hae = dexml2.fields.Float()
    ce = dexml2.fields.Float()
    le = dexml2.fields.Float()


class Detail(dexml2.Model):
    class meta:
        tagname = 'detail'


class Event(dexml2.Model):
    class meta:
        tagname = 'event'
    version = dexml2.fields.Float()
    type = dexml2.fields.String()
    uid = dexml2.fields.String()
    time = dexml2.fields.String()
    start = dexml2.fields.String(required=False)
    stale = dexml2.fields.String(required=False)
    point = dexml2.fields.Model(Point, required=False)  # FIXME
    detail = dexml2.fields.Model(Detail, required=False)
    access = dexml2.fields.String(required=False)
    qos = dexml2.fields.String(required=False)
    opex = dexml2.fields.String(required=False)
    how = dexml2.fields.String()


class EventType(object):

    describes = None
    type_fields = []

    def __init__(self, event_type=None):
        self.event_type = event_type
        split_event = event_type.split('-')
        d = dict(zip(self.type_fields[0:len(split_event)], split_event))
        for k, v in d.iteritems():
            setattr(self, k, v)

    def __str__(self):
        return self.event_type


class AtomEventType(EventType):
    describes = 'Thing'
    type_fields = ['_describes', 'affiliation', 'battle_dimension', 'function']


class DataEventType(EventType):
    describes = 'Data'
    type_fields = ['_describes', 'dimension']
