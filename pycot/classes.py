#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Python Cursor on Target Module Class Definitions."""

import logging
import os
import socket
import time

import gexml

import pycot

__author__ = 'Greg Albrecht W2GMD <oss@undef.net>'
__copyright__ = 'Copyright 2020 Orion Labs, Inc.'
__license__ = 'Apache License, Version 2.0'


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


class Detail(gexml.Model):
    """CoT Detail"""
    class meta:  # NOQA pylint: disable=invalid-name,missing-class-docstring,too-few-public-methods
        tagname = 'detail'
    uid = gexml.fields.Model(UID, required=False)
    contact = gexml.fields.Model(Contact, required=False)
    track = gexml.fields.Model(Track, required=False)
    remarks = gexml.fields.Model(Remarks, required=False)


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


# Dear Reader, Py3 doesn't need to inherit from Object anymore!
class NetworkClient:
    """CoT Network Client (TX)."""

    _logger = logging.getLogger(__name__)
    if not _logger.handlers:
        _logger.setLevel(pycot.LOG_LEVEL)
        _console_handler = logging.StreamHandler()
        _console_handler.setLevel(pycot.LOG_LEVEL)
        _console_handler.setFormatter(pycot.LOG_FORMAT)
        _logger.addHandler(_console_handler)
        _logger.propagate = False

    def __init__(self, cot_host: str, cot_port: int = None,
                 broadcast: bool = False) -> None:
        self.broadcast = broadcast

        self.socket: socket.socket = None
        self.addr: str = None
        self.port: int = None

        if ':' in cot_host:
            self.addr, port = cot_host.split(':')
            self.port = int(port)
        elif cot_port:
            self.addr = cot_host
            self.port = int(cot_port)
        else:
            self.addr = cot_host
            self.port = int(pycot.DEFAULT_COT_PORT)

        self.socket_addr = f'{self.addr}:{self.port}'
        self._logger.info('Using CoT Host %s', self.socket_addr)

        if self.broadcast:
            self._setup_broadcast_socket()
        else:
            self._setup_unicast_socket()

    def _setup_unicast_socket(self) -> None:
        """Sets up the TCP Unicast Socket for sending CoT events."""
        self._logger.debug('Setting up Unicast Socket.')
        if self.socket is not None:
            self.socket.close()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.addr, self.port))

    def _setup_broadcast_socket(self) -> None:
        """Sets up the UDP Broadcast Socket for sending CoT events."""
        self._logger.debug('Setting up Broadcast Socket.')
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    def send_cot(self, event: bytes, timeout: int = 1) -> bool:
        """Wrapper for sending TCP Unicast or UDP Broadcast CoT Events."""
        if os.environ.get('DONT_ADD_NEWLINE'):
            _event = event
        else:
            _event = event + b'\n'

        self._logger.debug('Sending CoT to %s: "%s"', self.socket_addr, _event)

        if self.broadcast:
            return self.sendto(_event)
        else:
            return self.sendall(_event, timeout)

    def close(self):
        self.socket.close()

    def sendall(self, event: bytes, timeout: int = 1) -> bool:
        """Sends a CoT Event to a TCP Unicast address."""
        # is the socket alive?
        assert self.socket.fileno() is not -1

        self.socket.settimeout(timeout)

        try:
            self.socket.sendall(event)
            return True
        except Exception as exc:
            self._logger.error(
                'socket.sendall() raised an Exception, sleeping: ')
            self._logger.exception(exc)
            # TODO: Make this value configurable, or add ^backoff.
            time.sleep(2)
            self._setup_unicast_socket()
            return False

    def sendto(self, event: bytes) -> bool:
        """Sends a CoT Event to a UDP Broadcast address."""
        try:
            self.socket.sendto(event, (self.addr, self.port))
            return True
        except Exception as exc:
            self._logger.error(
                'socket.sendto() raised an Exception, sleeping: ')
            self._logger.exception(exc)
            # TODO: Make this value configurable, or add ^backoff.
            time.sleep(2)
            self._setup_broadcast_socket()
            return False
