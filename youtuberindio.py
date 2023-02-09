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


'''comando = [
{   "command":"start",
    "description":"Inicias el bot"},

{   "command":"help",
    "description":"centro de ayuda"},      OTRA FORMA DE ENVIAR COMANDOS

{   "command":"support",
    "description":"Servicio de soporte"}
]
comando=json.dumps(comando)
url=url+str(comando)
response=requests.get(url)
print(response)'''
comando=[("start","descripcion del inicio"),("help","pedir ayuda"),("finalizar","terminar alguna cosa"),("gettime","Obtener el tiempo"),("button", "Prueba de botones")]

def message_handler(update, context):
    user_message=update.message.text
    print(user_message) #Imprimir mensaje en la consola python
    if(user_message.startswith('/')):
        update.message.reply_text("Comando no valido")  
    else:  
        update.message.reply_text(f'You send the following: {user_message}') #Enviar mensaje dentro del bot telegram
        user_info=update.message
        print(user_info)
        print("#############################")
        print(user_message)

def photo_handler(update, context):
    update.message.reply_text(f'Respuesta automatica para fotos') 

def start(update,context):
    user_info=update.message
    update.message.reply_text(f'{user_info.from_user.username} Bienvenido al nuevo bot')

def get_time(update, context):
    print(update.message.text)
    now=datetime.now()
    dt_string=now.strftime("%d/%m/%y_%H:%M:%S")
    update.message.reply_text(f'Current time is: {dt_string}')
    print(comando)


def main_menu_handler(update, context):
    user_info=update.message
    update.message.reply_text(f'{user_info.from_user.username} este es el menu del boton')
    # Create the button
    button1 = InlineKeyboardButton("button1", callback_data="button_1")
    button2 = InlineKeyboardButton("button2", callback_data="button_2")
    button3 = InlineKeyboardButton("back", callback_data="back")


    # Create the keyboard
    keyboard = [[button1, button2], [button3]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send the message with the button
    bot.send_message(chat_id=chat_id, text="Press the button:", reply_markup=reply_markup)
    updater = Updater(token=api_key, use_context=True)
    updater.dispatcher.add_handler(CallbackQueryHandler(button_handler))

def button_handler(update,context):
    query = update.callback_query
    if query.data == "button_1":
        bot.answer_callback_query(callback_query_id=query.id, text="Button 1 pressed")
    elif query.data == "button_2":
        bot.answer_callback_query(callback_query_id=query.id, text="Button 2 pressed")
    elif query.data == "back":
        bot.answer_callback_query(callback_query_id=query.id, text="Back pressed")


def main():
    t_bot=Bot(api_key)
    updater=Updater(bot=t_bot, use_context=True)
    comando=[("start","Iniciar el bot"),("help","Comandos de bot"),("finalizar","terminar alguna cosa"),("gettime","Obtener el tiempo"),("button", "ensayo del boton")]
    t_bot.set_my_commands(comando)
    dp=updater.dispatcher
    dp.add_handler(MessageHandler(filters=Filters.text & (~Filters.command), callback=message_handler))
    dp.add_handler(CommandHandler("gettime", get_time))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("button", main_menu_handler)) 
    updater.dispatcher.add_handler(CallbackQueryHandler(button_handler))   
    updater.start_polling()
    updater.idle()



if __name__=='__main__':
    main()