#!usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from unittest import TestCase
from unittest import mock
import time

import telegram as tg

import tgbot


def next_id():
    return int(time.time() * 1000000)


class TestTgbot(TestCase):

    def fake_bot(self):
        bot = mock.Mock()
        return bot

    def fake_user(self, is_bot=False):
        user = tg.User(next_id(), 'user', is_bot)
        return user

    def fake_message(self, text, bot, **params):
        msg = tg.Message(next_id(),
                         chat=tg.Chat(next_id(), 'chat'),
                         text=text,
                         date=datetime.datetime.utcnow(),
                         bot=bot,
                         **params
                        )
        return msg

    def test_cmd_chat_id(self):
        bot = self.fake_bot()
        msg = self.fake_message('/chatid',
                                bot=bot,
                                from_user=self.fake_user()
                                )
        msg_id = msg.message_id
        chat_id = msg.chat.id
        reply = 'Current chat id is {}'.format(chat_id)
        update = tg.Update(update_id=next_id(), message=msg)

        tgbot.chat_id(bot, update)
        bot.send_message.assert_called_once_with(chat_id,
                                                 reply,
                                                 reply_to_message_id=msg_id)

    def test_handler_kick_user(self):
        bot = self.fake_bot()
        new_chat_members = [self.fake_user(is_bot=True), self.fake_user()]
        msg = self.fake_message('',
                                bot=bot,
                                from_user=self.fake_user(),
                                new_chat_members=new_chat_members
                                )
        msg_id = msg.message_id
        chat_id = msg.chat.id
        update = tg.Update(update_id=next_id(), message=msg)

        tgbot.kick_user(bot, update)
        bot.kick_chat_member.assert_called_once_with(chat_id, new_chat_members[0].id)
