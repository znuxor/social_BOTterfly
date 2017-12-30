#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socialbotterfly

# start by processing messages

redditwrapper = socialbotterfly.RedditWrapper()
dbwrapper = socialbotterfly.DBWrapper()
messageprocessor = socialbotterfly.MessageProcessor(redditwrapper, dbwrapper)
messageprocessor.process_all_messages()
