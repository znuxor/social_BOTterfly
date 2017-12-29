#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .context import socialbotterfly

# This file contains the tests for the redditwrapper module

def test_initialization():
    wrapper_obj = socialbotterfly.InformationManager()

def test_file_loc_getter_no_error():
    wrapper_obj = socialbotterfly.InformationManager()
    wrapper_obj.get_database_file_location()

def test_logger_getter_no_error():
    wrapper_obj = socialbotterfly.InformationManager()
    wrapper_obj.get_project_logger()

def test_secrets_getter_no_exception():
    wrapper_obj = socialbotterfly.InformationManager()
    wrapper_obj.get_secrets()
