#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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

    def send_help_message(author, failure_information):
        with 
        help_message = 
