#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import functools
import logging
import os
import re
import traceback

from telegram.ext import CommandHandler
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import Updater
from telegram.ext.dispatcher import run_async

import env


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi, welcome to this telegram group!')


def help(bot, update):
    """Send a message when the command /help is issued."""
    text = '''
I can help when you're in need, please see the manual.

You can control me by sending these commands:

/help - show this message.
/echo - echo what you've sent.
/chatid - show current chat id.
'''
    update.message.reply_text(text)


def echo(bot, update):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def kick_user(bot, update):
    """Kick user out of chat."""
    # NOTE: Disable privacy mode in groups, so this bot can receive
    # all messages that people send to groups.
    # NOTE: Set your bot as admin first for required permission.
    # Kick out newly joined users when they're bots.
    members = update.message.new_chat_members
    for i in members:
        # kick bot only
        if i.is_bot and i.id != bot.id:
            logger.info('Kick bot: {uid},{username}'.format(uid=i.id, username=i.first_name))
            bot.kick_chat_member(update.message.chat.id, i.id)


def chat_id(bot, update):
    """Id of current chat."""
    chatid = update.message.chat.id
    text = 'Current chat id is {}'.format(chatid)
    update.message.reply_text(text)


def main():
    # Create the Updater and pass it your bot's token.
    token = env.must_get('TELEGRAM_BOT_TOKEN')
    # Initial updater
    # NOTE: Perfomance optimization, see https://github.com/python-telegram-bot/python-telegram-bot/wiki/Performance-Optimizations
    updater = Updater(token, request_kwargs={'read_timeout': 6, 'connect_timeout': 7})

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", run_async(start)))
    dp.add_handler(CommandHandler("help", run_async(help)))
    dp.add_handler(CommandHandler("echo", run_async(echo)))
    dp.add_handler(CommandHandler("chatid", run_async(chat_id)))
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, run_async(kick_user)))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
