#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Wrapper to make useful functions around PRAW, the core of the bot.'''

import datetime
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
        assert test_username == bot_username, 'Could not authenticate account!'

    def manage_post(self):
        '''Creates the weekly post and stickies it if the time has come.'''
        last_post_date = InformationManager().get_last_post_date()
        current_date = datetime.datetime.now().date()
        current_day = current_date.strftime('%A')
        been_a_week = (current_date - last_post_date) >= datetime.timedelta(7)
        if been_a_week and current_day == 'Sunday':
            # create post information
            installment_number = InformationManager().get_installment_number()
            challenge_1 = InformationManager().get_challenge_first()
            challenge_2 = InformationManager().get_challenge_second()
            week_first_day = (
                current_date + datetime.timedelta(1)).strftime("%D")
            title = 'Socialskills challenge for the week {}'.format(
                week_first_day)

            template = InformationManager().get_template_post()
            content = template.format(installment_number,
                                      challenge_1.content,
                                      challenge_1.author,
                                      challenge_2.content,
                                      challenge_2.author)

            # submit post
            bot_subreddit_name = InformationManager.get_subreddit_name()
            post = self.reddit.subreddit(bot_subreddit_name).submit(
                title, content, send_replies=False)
            post_id = post.id

            # distinction replacement
            InformationManager().get_last_post().distinguish(how='no')
            post.distinguish()

            # save and update info
            InformationManager().replace_post_id(post_id)
            InformationManager().consume_challenge()
            InformationManager().consume_challenge()

    def manage_comments(self):
        '''Manages the comments of the last post to award points'''
        post_id = InformationManager.get_last_post_id()
        last_post_item = praw.models.Submission(id=post_id)

        for a_top_comment in last_post_item.comments():
            content = a_top_comment.body
            author = a_top_comment.author
            for a_line in content.split('\n'):
                cleaned_line = a_line.strip()
                if '1:' in cleaned_line and cleaned_line.split() >= 5 and \
                        not InformationManager().has_point(author, post_id, 1):
                    InformationManager().award_point(author, post_id, 1,
                                                     InformationManager().get_challenge_score(1))
                if '2:' in cleaned_line and cleaned_line.split() >= 5 and \
                        not InformationManager().has_point(author, post_id, 2):
                    InformationManager().award_point(author, post_id, 2,
                                                     InformationManager().get_challenge_score(2))

                    if InformationManager().score_needs_update(author):
                        subreddit = self.reddit.subreddit(
                            InformationManager.get_subreddit_name())
                        subreddit.flair.set(author, '{} ☆'.format(
                            InformationManager().get_user_score(author)))
                        InformationManager().mark_score_updated(author)
