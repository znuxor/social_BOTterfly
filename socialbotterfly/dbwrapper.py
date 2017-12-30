#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sqlite3
import datetime
from .informationmanager import InformationManager
schema_filepath = 'dbschema.sql'
absolute_scheme_filepath = os.path.join(
    os.path.dirname(__file__), schema_filepath)


class DBWrapper():
    ''' Wrapper class around a database to interface the necessary operations.'''

    def __init__(self):

        if not os.path.exists(InformationManager().get_database_file_location()):
            print('Database does not exist, creating...')
            self.create_database(InformationManager().get_database_file_location())

        self.db_connection = sqlite3.connect(InformationManager().get_database_file_location())

    def create_database(self, database_file_path):
        ''' Creates the database file and sets the schema.'''
        self.db_connection = sqlite3.connect(database_file_path)
        with open(absolute_scheme_filepath) as file_handle:
            schema = file_handle.read()
            self.db_connection.executescript(schema)
        self.db_connection.close()

    def get_users_in_zone(self, zone_id):
        ''' Gets a list of all users in the same timezone and their data.'''
        command = """
        select * WHERE zone_id=? order by last_suggestion
        AND
        banned=false
        AND
        unsubscribed=false
        """
        self.db_connection.execute(command, (zone_id,))
        user_data = [i for i in self.db_connection.fetchmany()]
        print(user_data)
        return user_data

    def fetch_user(self, username):
        ''' Fetches a user's data from the database.'''
        command = """
        select * where nickname=?
        """
        self.db_connection.execute(command, (username, ))
        user_data = self.db_connection.fetch()
        print(user_data)
        return user_data

    def add_user(self, username, latitude, longitude, zone_id, max_distance_km, banned=False, favourite_things='', blacklist_things=''):
        ''' Adds a user to the database.'''
        command = """
        INSERT into user_data (nickname, latitude, longitude, zone_id, max_distance_km, unsubscribed, banned, favourite_things, blacklist_things, last_suggestion, already_suggested)
        values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        self.db_connection.execute(command, (username, latitude, longitude, zone_id, max_distance_km, False, banned,
                                             favourite_things, blacklist_things, suggestion_freq, datetime.datetime.utcnow().strftime('%Y-%m-%d'), ''))

    def unsubscribe_user(self, username):
        ''' Marks a user as unsubscribed'''
        command = """
        UPDATE user_data
        SET unsubscribed=True
        WHERE nickname=?
        """
        self.db_connection.execute(command, (username,))

    def ban_user(self, username):
        ''' Marks a user as unsubscribed'''
        command = """
        UPDATE user_data
        SET banned=True
        WHERE nickname=?
        """
        self.db_connection.execute(command, (username,))

    def set_position(self, username, latitude, longitude, zone_id):
        ''' Changes a user's position'''
        command = """
        UPDATE user_data
        SET latitude=?, longitude=?, zone_id=?
        WHERE nickname=?
        """
        self.db_connection.execute(
            command, (latitude, longitude, zone_id, username))

    def set_max_distance(self, username, max_distance_km):
        ''' Changes a user's max distance'''
        command = """
        UPDATE user_data
        SET max_distance_km=?
        WHERE nickname=?
        """
        self.db_connection.execute(command, (max_distance_km, username))

    def set_favourite_things(self, username, favourite_things):
        ''' Changes a user's favourite things'''
        command = """
        UPDATE user_data
        SET favourite_things=?
        WHERE nickname=?
        """
        self.db_connection.execute(command, (favourite_things, username))

    def set_blacklist_things(self, username, blacklist_things):
        ''' Changes a user's favourite things'''
        command = """
        UPDATE user_data
        SET blacklist_things=?
        WHERE nickname=?
        """
        self.db_connection.execute(command, (blacklist_things, username))

    def update_with_suggestion(self, username, suggestion):
        command = """
        UPDATE user_data
        SET 
        WHERE nickname=?
        """
        self.db_connection.execute(command, (username))

    def cleanup_inactive_users(self, username):
        raise NotImplemented

    def __delete__(self, instance):
        self.db_connection.commit()
        self.db_connection.close()
