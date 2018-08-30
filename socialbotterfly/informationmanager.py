#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Contains the definition of the information management interface.'''

import os
import logging
import pickle

PROJECT_DATA_PATH = os.path.join('.')


class InformationManager():
    '''Serves as an abstraction layer with saved data and secrets.'''

    # singleton stuff
    __instance = None

    def __new__(cls):
        if InformationManager.__instance is None:
            InformationManager.__instance = object.__new__(cls)
        return InformationManager.__instance

    def __init__(self):

        # logger initialization
        log_file_path = os.path.join(PROJECT_DATA_PATH, 'log.txt')
        logging.basicConfig(filename=log_file_path, level=logging.DEBUG)
        self.logger = logging.getLogger()

        # secrets loading
        secrets_file_path = os.path.join(PROJECT_DATA_PATH, 'secrets.p')
        if not os.path.exists(secrets_file_path):
            self.secrets = None
        else:
            with open(secrets_file_path, 'rb') as file_handle:
                self.secrets = pickle.load(file_handle)

    def get_project_logger(self):
        ''' Returns the logger object'''
        return self.logger

    def get_secrets(self):
        ''' Returns the secrets'''
        return self.secrets
