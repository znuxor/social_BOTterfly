#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import logging
import pickle

project_name = 'socialbotterfly'
project_data_path = os.path.join(os.path.expanduser('~'), '.'+project_name)


class InformationManager(object):

    # singleton stuff
    __instance = None

    def __new__(cls):
        if InformationManager.__instance is None:
            InformationManager.__instance = object.__new__(cls)
        return InformationManager.__instance

    def __init__(self):
        # checks if the data directory exists, if not, we create it
        if not os.path.exists(project_data_path):
            os.mkdir(project_data_path)

        # db file location
        self.db_file_loc = os.path.join(project_data_path, 'user_data.db')

        # logger initialization
        log_file_path = os.path.join(project_data_path, 'log.txt')
        logging.basicConfig(filename=log_file_path,level=logging.DEBUG)
        self.logger = logging.getLogger()

        # secrets loading
        secrets_file_path = os.path.join(project_data_path, 'secrets.p')
        if not os.path.exists(secrets_file_path):
            self.secrets = None
        else:
            with open(secrets_file_path, 'rb') as f:
                self.secrets = pickle.load(f)

    def get_project_logger(self):
        ''' Returns the logger object'''
        return self.logger

    def get_secrets(self):
        ''' Returns the secrets'''
        return self.secrets
