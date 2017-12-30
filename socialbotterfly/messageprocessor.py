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
        all_needed_info_available = False

        if all_needed_info_available:
            self.dbwrapper.add_user(author, latitude, longitude, zone_id, max_distance_km,favourite_things=favourite_things, blacklist_things=blacklist_things, suggestion_freq=suggestion_freq, communities=communities)
            self.redditwrapper.send_message(author, 'subscription successful', 'Your subscription was successful, be prepared to receive suggestion soon!')
        return True, None

    def process_unsubscribe_message(self, author):
        self.dbwrapper.unsubscribe_user(author)
        self.redditwrapper.send_message(author, 'unsubscription successful', 'Your unsubscription was successful')
        return True, None

    def process_comment_message(self, author, body):
        the_logger = InformationManager().get_project_logger()
        the_logger.info("Comment by /u/"+author + ": " + body)
        self.redditwrapper.send(author, 'Thank you for your comment!', 'Thank you for your comment for social_BOTterfly!')
        return True, None
