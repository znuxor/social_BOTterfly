#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import praw
from .informationmanager import InformationManager

class RedditWrapper():
    ''' Wrapper class around reddit to interact with the bot account.'''

    def __init__(self):
        secrets = InformationManager().get_secrets()
        client_id = secrets['client_id']
        client_secret = secrets['client_secret']
        bot_username = 'social_BOTterfly'
        bot_password = secrets['bot_password']
        self.reddit = praw.Reddit(client_id=client_id,
                                  client_secret=client_secret,
                                  username=bot_username,
                                  password=bot_password,
                                  user_agent='social_BOTterfly by /u/znuxor')
        test_username = self.reddit.user.me()
        assert test_username == bot_username, 'Could not authenticate to the bot account!'

    def has_unread_messages(self):
        '''Returns True if there is messages to process'''
        return len(list(self.reddit.inbox.unread(limit=1))) == 1

    def serve_oldest_message(self):
        '''Returns the following information about the oldest inbox message:
           author_username as string
           message_subject as string
           message_body as string
           message_id as string, used to mark a message as read after processing
        '''
        unread_message = [i for i in self.reddit.inbox.unread(limit=None)][-1]
        author_username = unread_message.author.name
        message_subject = unread_message.subject
        message_body = unread_message.body
        message_id = unread_message.id
        return author_username, message_subject, message_body, message_id

    def mark_as_read(self, message_id):
        ''' Mark a message as read, takes the reddit PRAW message id as argument'''
        message_obj = self.reddit.inbox.message(message_id)
        message_obj.mark_read()

    def send_message(self, user_name, subject, body):
        ''' Sends a message to a redditor'''
        self.reddit.redditor(user_name).message(subject, body)
