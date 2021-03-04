#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Python Cursor on Target Module Class Definitions."""

import datetime
import uuid

import gexml

__author__ = "Greg Albrecht W2GMD <oss@undef.net>"
__copyright__ = "Copyright 2020 Orion Labs, Inc."
__license__ = "Apache License, Version 2.0"


class Point(gexml.Model):
    """CoT Point"""
    class meta:  # NOQA pylint: disable=invalid-name,missing-class-docstring,too-few-public-methods
        tagname = 'point'
    lat = gexml.fields.Float()
    lon = gexml.fields.Float()
    hae = gexml.fields.Float(required=False)
    ce = gexml.fields.Float()
    le = gexml.fields.Float()
    version = gexml.fields.String(required=False)


class UID(gexml.Model):
    """CoT UID"""
    class meta:  # NOQA pylint: disable=invalid-name,missing-class-docstring,too-few-public-methods
        tagname = 'uid'
    Droid = gexml.fields.String()
    version = gexml.fields.String(required=False)


class Contact(gexml.Model):
    """CoT Contact"""
    class meta:  # NOQA pylint: disable=invalid-name,missing-class-docstring,too-few-public-methods
        tagname = 'contact'
    callsign = gexml.fields.String(required=False)
    freq = gexml.fields.String(required=False)
    email = gexml.fields.String(required=False)
    dsn = gexml.fields.String(required=False)
    phone = gexml.fields.String(required=False)
    modulation = gexml.fields.String(required=False)
    hostname = gexml.fields.String(required=False)
    version = gexml.fields.String(required=False)


class ChatGroup(gexml.Model):
    class meta:
        tagname = 'chatgrp'
    uid0 = gexml.fields.String(required=False)
    uid1 = gexml.fields.String(required=False)
    id = gexml.fields.String(required=False)


class Chat(gexml.Model):
    """CoT Chat"""
    class meta:
        tagname = '__chat'
    senderCallsign = gexml.fields.String(required=False)
    chatroom = gexml.fields.String(required=False)
    groupOwner = gexml.fields.String(required=False)
    id = gexml.fields.String(required=False)
    parent = gexml.fields.String(required=False)
    chatgrp = gexml.fields.Model(ChatGroup, required=False)


class Track(gexml.Model):
    """CoT Track"""
    class meta:  # NOQA pylint: disable=invalid-name,missing-class-docstring,too-few-public-methods
        tagname = 'track'
    course = gexml.fields.String()
    speed = gexml.fields.String()
    slope = gexml.fields.String(required=False)
    eCourse = gexml.fields.String(required=False)
    eSpeed = gexml.fields.String(required=False)
    eSlope = gexml.fields.String(required=False)
    version = gexml.fields.String(required=False)


class Remarks(gexml.Model):
    """CoT Track"""
    class meta:  # NOQA pylint: disable=invalid-name,missing-class-docstring,too-few-public-methods
        tagname = 'remarks'
    value = gexml.fields.String(tagname='.', required=False)
    source = gexml.fields.String(required=False)
    time = gexml.fields.String(required=False)
    to = gexml.fields.String(required=False)
    keywords = gexml.fields.String(required=False)
    version = gexml.fields.String(required=False)


class Link(gexml.Model):
    class meta:
        tagname = "link"
    uid = gexml.fields.String(required=False)
    production_time = gexml.fields.String(required=False)
    event_type = gexml.fields.String(attrname="type")
    url = gexml.fields.String(required=False)
    parent_callsign = gexml.fields.String(required=False)
    remarks = gexml.fields.String(required=False)
    mime = gexml.fields.String(required=False)
    version = gexml.fields.String(required=False)
    relation = gexml.fields.String(required=False)


class Detail(gexml.Model):
    """CoT Detail"""
    class meta:  # NOQA pylint: disable=invalid-name,missing-class-docstring,too-few-public-methods
        tagname = 'detail'
    uid = gexml.fields.Model(UID, required=False)
    contact = gexml.fields.Model(Contact, required=False)
    track = gexml.fields.Model(Track, required=False)
    remarks = gexml.fields.Model(Remarks, required=False)
    link = gexml.fields.Model(Link, required=False)
    chat = gexml.fields.Model(Chat, required=False)


class Event(gexml.Model):
    """CoT Event Object"""
    class meta:  # NOQA pylint: disable=invalid-name,missing-class-docstring,too-few-public-methods
        tagname = 'event'

    __str__ = gexml.Model.render

    version = gexml.fields.String(required=True)  # default="2.0"
    event_type = gexml.fields.String(attrname="type")

    uid = gexml.fields.String(required=True)  # default=uuid.uuid4()

    time = gexml.fields.DateTime(required=True)  # NOQA default=datetime.datetime.now(datetime.timezone.utc)
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

test_chat = """
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<event version="2.0" uid="GeoChat.FFF-1" type="b-t-f" time="2020-11-15T07:40:58.816Z" start="2020-11-15T07:40:58.816Z" stale="2020-11-16T07:40:58.816Z" how="h-g-i-g-o"><point lat="0.0" lon="0.0" hae="9999999.0" ce="9999999.0" le="9999999.0"/><detail><link uid="AAA-1" type="a-f-G-U-C" relation="p-p"/><__chat parent="RootContactGroup" groupOwner="false" chatroom="All Chat Rooms" id="All Chat Rooms" senderCallsign="FFF-1"><chatgrp uid0="FFF-1" uid1="All Chat Rooms" id="All Chat Rooms"/></__chat><remarks source="FFF-1" to="All Chat Rooms" time="2020-11-15T07:40:58.816Z">FFF-1</remarks><__serverdestination destinations="172.17.2.246:8087:tcp:FFF-1"/></detail></event>
"""
