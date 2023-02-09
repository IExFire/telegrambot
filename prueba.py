#https://api.telegram.org/bot6259775919:AAGS1aCvDUk9vCiqlBbDN6j2xdISZbNud2Q/getUpdates
#6259775919:AAGS1aCvDUk9vCiqlBbDN6j2xdISZbNud2Q
#Chatid: -815826376
#https://api.telegram.org/bot6259775919:AAGS1aCvDUk9vCiqlBbDN6j2xdISZbNud2Q/sendMessage?chat_id=-815826376&text=test message from python api

from telegram import Update,Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater,MessageHandler,Filters, CommandHandler, CallbackQueryHandler
from telegram.utils.request import Request
import requests, json
from datetime import datetime
import telegram

api_key = "6259775919:AAGS1aCvDUk9vCiqlBbDN6j2xdISZbNud2Q"
bot = telegram.Bot(api_key)
url="https://api.telegram.org/bot6259775919:AAGS1aCvDUk9vCiqlBbDN6j2xdISZbNud2Q/setMyCommands?commands="
chat_id = 2126628091

def main_menu_handler(update, context):
    # Create the menu buttons
    button1 = InlineKeyboardButton("Button 1", callback_data="button_1")
    button2 = InlineKeyboardButton("Button 2", callback_data="button_2")
    button3 = InlineKeyboardButton("Button 3", callback_data="button_3")
    
    # Create the menu keyboard
    keyboard = [[button1, button2], [button3]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Send the menu message with the keyboard
    bot.send_message(chat_id=2126628091, text="Choose an option:", reply_markup=reply_markup)

def button_handler(update,context):
    query = update.callback_query
    if query.data == "button_1":
        # Do something for button 1
        bot.answer_callback_query(callback_query_id=query.id, text="Button 1 pressed")
    elif query.data == "button_2":
        # Do something for button 2
        bot.answer_callback_query(callback_query_id=query.id, text="Button 2 pressed")
    elif query.data == "button_3":
        # Do something for button 3
        bot.answer_callback_query(callback_query_id=query.id, text="Button 3 pressed")

updater = Updater(token="6259775919:AAGS1aCvDUk9vCiqlBbDN6j2xdISZbNud2Q", use_context=True)

# Add the main menu handler to the dispatcher
updater.dispatcher.add_handler(CommandHandler("start", main_menu_handler))

# Add the button handler to the dispatcher
updater.dispatcher.add_handler(CallbackQueryHandler(button_handler))

# Start the bot
updater.start_polling()
