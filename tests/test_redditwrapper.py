#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .context import socialbotterfly
from socialbotterfly import redditwrapper

# This file contains the tests for the redditwrapper module


def test_initialization():
    wrapper_obj = socialbotterfly.redditwrapper.RedditWrapper()


def test_has_unread_message_no_error():
    wrapper_obj = socialbotterfly.redditwrapper.RedditWrapper()
    wrapper_obj.has_unread_messages()


def test_serve_oldest_message_no_error():
    wrapper_obj = socialbotterfly.redditwrapper.RedditWrapper()
    wrapper_obj.serve_oldest_message()
