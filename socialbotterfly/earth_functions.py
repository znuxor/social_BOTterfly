#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sqrt, sin, cos, atan2

EARTH_RADIUS = 6371

def get_great_circle_distance(longitude_a, latitude_a, longitude_b, latitude_b):
    # see https://en.wikipedia.org/wiki/Great-circle_distance#Computational_formulas
    phi1 = longitude_a
    phi2 = longitude_b
    lambda1 = latitude_a
    lambda2 = latitude_b
    delta_phi = abs(phi1 - phi2)
    delta_lambda = abs(lambda1 - lambda2)

    numerator = sqrt(
            (cos(phi2)* sin(delta_lambda))**2 + (cos(phi1)*sin(phi2)-sin(phi1)*cos(phi2)*cos(delta_lambda))**2
            )

    denominator = sin(phi1)*sin(phi2)+cos(phi1)*cos(phi2)*cos(delta_lambda)
    central_angle = atan2(numerator/denominator)
    distance = central_angle * EARTH_RADIUS

    return distance
