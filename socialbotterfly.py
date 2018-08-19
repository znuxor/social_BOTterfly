#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socialbotterfly
import time

LONG_PAUSE = 10*60

redditwrapper = socialbotterfly.RedditWrapper()
redditwrapper.manage_post()
redditwrapper.manage_comments()
