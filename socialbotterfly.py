#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Main file, drives the bot between its states'''

import socialbotterfly

redditwrapper = socialbotterfly.RedditWrapper()
redditwrapper.manage_post()
redditwrapper.manage_comments()
