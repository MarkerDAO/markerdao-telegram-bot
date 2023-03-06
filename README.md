# Telegram Bot 

This telegram bot can reply message in telegram group when being @your_bot_name

## Installation

```bash
pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
```

## Usage

- register a telegram bot using @BotFather and get the bot TOKEN, register a OpenAI API account and get the API key, then set the TOKEN and key in config.env

- Please set telegram bot TOKEN, OpenAI API key and your telegram bot name in config.env in config dir before run the command as follows:

```bash
./bot.py
```

- Your bot on the server needs to be outside of GFW or enable proxy to access telegram bot API and OpenAI API

**WATCHOUT:** disable the privacy mode of your telegram bot https://stackoverflow.com/questions/45889405/how-to-read-messages-from-telegram-group-with-bot https://stackoverflow.com/questions/38565952/how-to-receive-messages-in-group-chats-using-telegram-bot-api  and give a admin of group before join the group, if it does not work well, you need to remove the bot from your group
and rejoin the group again.


## Helpful reference

- https://github.com/karfly/chatgpt_telegram_bot/blob/0779808db35e99541002b7d3aadf82d890797738/bot/bot.py#L86-L143
