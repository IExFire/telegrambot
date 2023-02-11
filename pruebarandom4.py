from telegram import Update,Bot, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater,MessageHandler,Filters, CommandHandler, CallbackQueryHandler
from telegram.utils.request import Request
import requests, json
from datetime import datetime
import telegram

#Generando un menu de botones luego de presionar un boton

api_key = "6259775919:AAGS1aCvDUk9vCiqlBbDN6j2xdISZbNud2Q"
bot = telegram.Bot(api_key)
url="https://api.telegram.org/bot6259775919:AAGS1aCvDUk9vCiqlBbDN6j2xdISZbNud2Q/setMyCommands?commands="


updater = Updater(token=api_key, use_context=True)
bot = updater.bot

# aquí puedes manejar la actualización y recibir el mensaje
def handle_message(update, context):
    chat_id = update.message.chat_id
    message_id = update.message.message_id
    text = "Este es un mensaje editado."
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text)

# aquí agregas el controlador de mensajes a un manejador
updater.dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))

# aquí inicias el bot
updater.start_polling()
updater.idle()

