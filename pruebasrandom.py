from telegram import Update,Bot, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater,MessageHandler,Filters, CommandHandler, CallbackQueryHandler
from telegram.utils.request import Request
import requests, json
from datetime import datetime
import telegram

api_key = "6259775919:AAGS1aCvDUk9vCiqlBbDN6j2xdISZbNud2Q"
bot = telegram.Bot(api_key)
url="https://api.telegram.org/bot6259775919:AAGS1aCvDUk9vCiqlBbDN6j2xdISZbNud2Q/setMyCommands?commands="
chat_id = 2126628091

bot = telegram.Bot(token=api_key)

def send_message_with_buttons(chat_id):
    button1 = KeyboardButton("Press me")
    reply_markup = ReplyKeyboardMarkup([[button1]])
    bot.send_message(chat_id=chat_id, text="Here's your button:", reply_markup=reply_markup)

def button_callback(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="Button pressed!")

updater = Updater(token=api_key, use_context=True)
dispatcher = updater.dispatcher

button_handler = CallbackQueryHandler(button_callback)
dispatcher.add_handler(button_handler)

updater.start_polling()