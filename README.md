Telegram Bot

#### Introduction

ICO projects usually use Telegram to build community, with its private, fast and free features.

With Telegram Bot, you can integrate some services into your user groups, such as automatically publishing scheduled notifications and news, interacting with users, providing information query through your own servers.

#### Getting started

This is just a starter, but you can go further by starting from here.

- new bot: [Introduction to the API](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Introduction-to-the-API)
- custom: add any command and implementation into [tgbot](tgbot.py)
- run: ```python tgbot.py```
- example features:
  - `/chatid` will reply current chat id. After got this chat id, you can actively send any messages to specified groups, and do any telegram group-based-access-control strategies.
  - kick out other bots. Bots are awesome, but some are not, you may have to kick other bots out to keep the group peace.

#### Performance

According to [Getting Updates](https://core.telegram.org/bots/api#getting-updates):

There are two mutually exclusive ways of receiving updates for your bot:
- [`getUpdates`](https://core.telegram.org/bots/api#getupdates) is pull
- [`Webhooks`](https://core.telegram.org/bots/api#setwebhook) is push

Use `getUpdates` is simple, and you can get started with this mechanism. But if your telegram group has been getting more and more intensive messages and your bot is getting slower, you may have to use Webhooks instead:
- Avoids your bot having to ask for updates frequently.
- Avoids the need for some kind of polling mechanism in your code.

For details, please read through [Marvin's Marvellous Guide to All Things Webhook](https://core.telegram.org/bots/webhooks).

#### Reference

- [Telegram Messenger](https://telegram.org/)
- [Bots: An introduction for developers](https://core.telegram.org/bots)
- [Marvin's Marvellous Guide to All Things Webhook](https://core.telegram.org/bots/webhooks)
- [python-telegram-bot/python-telegram-bot: We have made you a wrapper you can't refuse](https://github.com/python-telegram-bot/python-telegram-bot)
- [Introduction to the API · python-telegram-bot/python-telegram-bot Wiki](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Introduction-to-the-API)
- [Extensions – Your first Bot · python-telegram-bot/python-telegram-bot Wiki](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions-%E2%80%93-Your-first-Bot)
- [solyarisoftware/BOTServer: http://telegram.org Bot API Webhooks Framework, for Rubyists](https://github.com/solyarisoftware/BOTServer)
