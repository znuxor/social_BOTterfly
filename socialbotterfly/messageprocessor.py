#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .informatiionmanager import InformationManager

help_message_filename = 'help_message.txt'
absolute_help_file_path = os.path.join(
        os.path.dirnam(__file__), help_message_filename)

class MessageProcessor():
    '''Classes that processes messages and does the actions needed'''
    def __init__(self, redditwrapper, dbwrapper):
        self.redditwrapper = redditwrapper
        self.dbwrapper = dbwrapper

    def process_all_messages(self):
        while self.redditwrapper.has_unread_messages():
            self.process_one_message()

    def process_one_message(self):
        author, body, message_id = self.redditwrapper.serve_oldest_message()
        subject_filtered = subject.lower().rstrip(' ').lstrip(' ')
        if subject_filtered == 'subscribe':
            valid, failure_information = self.process_subscribe_message(author, body)
        elif subject_filtered == 'unsubscribe':
            valid, failure_information = self.process_unsubscribe_message(author)
        elif subject_filtered == 'comment':
            valid, failure_information = self.process_comment_message(author, body)
        else:
            valid = False
            failure_information = None

        if valid == False:
            self.send_help_message(author)

        # mark the message as valid
        self.redditwrapper.mark_as_read(message_id)

    def send_help_message(self, author, failure_information):
        with  open(absolute_help_file_path, 'r') as f:
            help_message = f.read()
        self.redditwrapper.send_message(author, 'social_BOTterfly Help message', help_message.format(author, failure_information))

    def process_subscribe_message(self, author, body):
        error_message = 'Some information was missing:'
        all_needed_info_available = False
        latitude = None
        longitude = None
        zone_id = None
        max_distance_km = None
        favourite_things = ''
        blacklist_things = ''
        suggestion_freq = ''

        # Parse the message body for the necessary information
        lines = body.split('\n')
        #TODO

        if latitude is not None and longitude is not None and zone_id is not None and max_distance_km is not None:
            all_needed_info_available = True

        if all_needed_info_available:
            self.dbwrapper.add_user(author, latitude, longitude, zone_id, max_distance_km,favourite_things=favourite_things, blacklist_things=blacklist_things)
            self.redditwrapper.send_message(author, 'subscription successful', 'Your subscription was successful, be prepared to receive suggestion soon!')
            return True, None
        else:
            return False, error_message

    def process_unsubscribe_message(self, author):
        self.dbwrapper.unsubscribe_user(author)
        self.redditwrapper.send_message(author, 'unsubscription successful', 'Your unsubscription was successful')
        return True, None

    def process_comment_message(self, author, body):
        the_logger = InformationManager().get_project_logger()
        the_logger.info("Comment by /u/"+author + ": " + body)
        self.redditwrapper.send(author, 'Thank you for your comment!', 'Thank you for your comment for social_BOTterfly!')
        return True, None
