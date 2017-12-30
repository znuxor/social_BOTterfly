#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .context import socialbotterfly
from math import pi

# This file contains the tests for the redditwrapper module

EARTH_RADIUS = 6371
ALLOWED_DISCREPANCY = 1e-3


def test_same_position():
    zero_dist = socialbotterfly.get_great_circle_distance(0, 0, 0, 0)
    assert zero_dist < ALLOWED_DISCREPANCY


def test_north_south_poles():
    ns_dist = socialbotterfly.get_great_circle_distance(0, -90, 0, 90)
    assert (ns_dist - pi*EARTH_RADIUS) < ALLOWED_DISCREPANCY


def test_opposite_positions():
    opp_dist = socialbotterfly.get_great_circle_distance(-120, 0, 60, 0)
    assert (opp_dist - pi*EARTH_RADIUS) < ALLOWED_DISCREPANCY


def test_quarter_turn():
    quarter_dist = socialbotterfly.get_great_circle_distance(-30, 0, 60, 0)
    assert (quarter_dist - 0.5*pi*EARTH_RADIUS) < ALLOWED_DISCREPANCY
