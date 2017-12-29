#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .context import socialbotterfly
from socialbotterfly import redditwrapper

# This file contains the tests for the redditwrapper module

def test_initialization():
    wrapper_obj = socialbotterfly.redditwrapper.RedditWrapper()
