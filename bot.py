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

async def message_handle(update: Update, context: CallbackContext, message=None):
    message = update.message
    print("from telegram bot update message: ", message)
    print ("chat type: ", message.chat.type)
    message_text = message.text
    if message.chat.type == "group" and config.telegram_bot_name in message_text:
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