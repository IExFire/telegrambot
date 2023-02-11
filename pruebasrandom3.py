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
chat_id = 2126628091


def main_menu_handler(update, context):
    user_info=update.message
    update.message.reply_text(f'{user_info.from_user.username} este es el menu del boton')
    # Create the button
    button1 = InlineKeyboardButton("button1", callback_data="first_button")
    button2 = InlineKeyboardButton("button2", callback_data="button_2")
    button3 = InlineKeyboardButton("back", callback_data="back")

    # Create the keyboard
    keyboard = [[button1, button2], [button3]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send the message with the button
    bot.send_message(chat_id=update.message.chat_id, text="Press the button:", reply_markup=reply_markup)

def button_callback(update, context):
    query = update.callback_query
    if query.data == 'first_button':
        query.answer()
        keyboard = [[InlineKeyboardButton("Option 1", callback_data='option1'),
                     InlineKeyboardButton("Option 2", callback_data='option2')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text="Please choose an option:", reply_markup=reply_markup)
    elif query.data == 'option1':
        query.answer(text="You selected Option 1.")
    elif query.data == 'option2':
        query.answer(text="You selected Option 2.")

updater = Updater(token=api_key, use_context=True)
dispatcher = updater.dispatcher
start_handler = CommandHandler('start', main_menu_handler)
dispatcher.add_handler(start_handler)
callback_handler = CallbackQueryHandler(button_callback)
dispatcher.add_handler(callback_handler)

updater.start_polling()