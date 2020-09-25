#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Python Cursor on Target Module Class Definitions."""

import uuid

import gexml

__author__ = 'Greg Albrecht W2GMD <oss@undef.net>'
__copyright__ = 'Copyright 2020 Orion Labs, Inc.'
__license__ = 'Apache License, Version 2.0'


class Point(gexml.Model):
    class meta:
        tagname = 'point'
    lat = gexml.fields.Float()
    lon = gexml.fields.Float()
    hae = gexml.fields.Float()
    ce = gexml.fields.Float()
    le = gexml.fields.Float()


class UID(gexml.Model):
    class meta:
        tagname = 'uid'
    Droid = gexml.fields.String()


class Detail(gexml.Model):
    class meta:
        tagname = 'detail'
    uid = gexml.fields.Model(UID, required=False)


class Event(gexml.Model):
    class meta:
        tagname = 'event'

    __str__ = gexml.Model.render

    version = gexml.fields.Float()
    event_type = gexml.fields.String(attrname='type')

    # FIXME: This should be default=uuid.uuid4(), but declaring a default
    # also causes required=False, and so won't render correctly.
    uid = gexml.fields.String()

    time = gexml.fields.DateTime()
    start = gexml.fields.DateTime(required=False)
    stale = gexml.fields.DateTime(required=False)
    point = gexml.fields.Model(Point, required=False)  # FIXME
    detail = gexml.fields.Model(Detail, required=False)
    access = gexml.fields.String(required=False)
    qos = gexml.fields.String(required=False)
    opex = gexml.fields.String(required=False)
    how = gexml.fields.String()


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
    "a - atoms (anything you drop on your foot), based on MS2525B."
    describes = 'Thing'
    type_fields = ['_describes', 'affiliation', 'battle_dimension', 'function']


class DataEventType(EventType):
    describes = 'Data'
    type_fields = ['_describes', 'dimension']
