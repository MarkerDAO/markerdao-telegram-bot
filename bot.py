#!/usr/bin/env python3

import config

import telegram
from telegram import Update, User, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CallbackContext,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters
)
from telegram.constants import ParseMode, ChatAction

import chat_gpt
from lru import LRU
from datetime import datetime

check_question_times_dict = LRU(10000)

def check_question_times(username):
    today = datetime.now().strftime('%Y-%m-%d')
    key = username + today
    if not check_question_times_dict.has_key(key):
        check_question_times_dict[key] = 0
    count = check_question_times_dict[key]

    if count >= config.question_limit_per_user:
        return False
    else:
        check_question_times_dict[key] = count + 1
        return True


async def message_handle(update: Update, context: CallbackContext, message=None):
    message = update.message
    print("from telegram bot update message: ", message)
    print ("chat type: ", message.chat.type)
    message_text = message.text
    from_user = message.from_user.username
    print("from_user: ", from_user)

    if (message.chat.type == "group" or message.chat.type == "supergroup") and config.telegram_bot_name in message_text:
        if message.chat.username != "MarkerDAO":
            return
        if not check_question_times(from_user):
            await update.message.reply_text("You have reached the daily question limit per user.")
            return
        message_text = message_text.replace(config.telegram_bot_name, "")
        answer = chat_gpt.get_answer_from_chatgpt(message_text)
        print("answer: ", answer.strip())
        await update.message.reply_text(answer.strip())


def run_bot():
    application = (
        ApplicationBuilder()
        .token(config.telegram_bot_token)
        .build()
    )

    user_filter = filters.ALL
    
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND & user_filter, message_handle))
    # start the bot
    print("Bot started.")
    application.run_polling()

if __name__ == "__main__":
    run_bot()