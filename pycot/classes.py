#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Python Cursor on Target Module Class Definitions."""

import gexml

__author__ = 'Greg Albrecht W2GMD <oss@undef.net>'
__copyright__ = 'Copyright 2020 Orion Labs, Inc.'
__license__ = 'Apache License, Version 2.0'


class Point(gexml.Model):
    """CoT Point"""
    class meta:  # NOQA pylint: disable=invalid-name,missing-class-docstring,too-few-public-methods
        tagname = 'point'
    lat = gexml.fields.Float()
    lon = gexml.fields.Float()
    hae = gexml.fields.Float()
    ce = gexml.fields.Float()
    le = gexml.fields.Float()


class UID(gexml.Model):
    """CoT UID"""
    class meta:  # NOQA pylint: disable=invalid-name,missing-class-docstring,too-few-public-methods
        tagname = 'uid'
    Droid = gexml.fields.String()


class Detail(gexml.Model):
    """CoT Detail"""
    class meta:  # NOQA pylint: disable=invalid-name,missing-class-docstring,too-few-public-methods
        tagname = 'detail'
    uid = gexml.fields.Model(UID, required=False)


class Event(gexml.Model):
    """CoT Event Object"""
    class meta:  # NOQA pylint: disable=invalid-name,missing-class-docstring,too-few-public-methods
        tagname = 'event'

    __str__ = gexml.Model.render

    version = gexml.fields.Float()
    event_type = gexml.fields.String(attrname='type')

    uid = gexml.fields.String()

    time = gexml.fields.DateTime()
    start = gexml.fields.DateTime(required=False)
    stale = gexml.fields.DateTime(required=False)
    point = gexml.fields.Model(Point, required=False)
    detail = gexml.fields.Model(Detail, required=False)
    access = gexml.fields.String(required=False)
    qos = gexml.fields.String(required=False)
    opex = gexml.fields.String(required=False)
    how = gexml.fields.String()


class EventType:  # pylint: disable=too-few-public-methods
    """CoT EventType"""

    describes = None
    type_fields = []

    def __init__(self, event_type=None):
        self.event_type = event_type
        split_event = event_type.split('-')
        data = dict(zip(self.type_fields[0:len(split_event)], split_event))
        for key, val in data.items():
            setattr(self, key, val)

    def __str__(self):
        return self.event_type


class AtomEventType(EventType):  # pylint: disable=too-few-public-methods
    """CoT AtomEventType
    a - atoms (anything you drop on your foot), based on MS2525B.
    """
    describes = 'Thing'
    type_fields = ['_describes', 'affiliation', 'battle_dimension', 'function']


class DataEventType(EventType):  # pylint: disable=too-few-public-methods
    """CoT DataEventType"""
    describes = 'Data'
    type_fields = ['_describes', 'dimension']
