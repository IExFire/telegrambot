#https://api.telegram.org/bot6259775919:AAGS1aCvDUk9vCiqlBbDN6j2xdISZbNud2Q/getUpdates
#6259775919:AAGS1aCvDUk9vCiqlBbDN6j2xdISZbNud2Q
#Chatid: -815826376
#https://api.telegram.org/bot6259775919:AAGS1aCvDUk9vCiqlBbDN6j2xdISZbNud2Q/sendMessage?chat_id=-815826376&text=test message from python api

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
    if(user_message == "📟 Menu"):
        main_menu_handler(update,context)
    elif(user_message == "☎️ Help"):
        help_function(update,context)
    elif(user_message == "⏱ Get Time"):
        get_time(update, context)
    elif(user_message == "🔐 Finish"):
        update.message.reply_text("La ejecucion ha terminado con normalidad")
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
    update.message.reply_text(f'{user_info.from_user.username} Bienvenido al nuevo bot, si quieres conocer los comandos disponibles dale al menu o usa el comando /help')
    keyboard = [[KeyboardButton("📟 Menu "), KeyboardButton("☎️ Help")],
                [KeyboardButton("⏱ Get Time"), KeyboardButton("🔐 Finish")]]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    context.bot.send_message(chat_id=update.message.chat_id, text="Please choose:", reply_markup=reply_markup)

def help_function(update,context):
    update.message.reply_text("Los comandos disponibles son los siguientes:\n- /start - Inicializa el bot\n- /help - Te muestra una lista de comandos \n- /finalizar - Termina el bot \n- /menu - Realiza la prueba de los botones \n /gettime - Obtener el tiempo ")

def get_time(update, context):
    print(update.message.text)
    now=datetime.now()
    dt_string=now.strftime("%d/%m/%y_%H:%M:%S")
    update.message.reply_text(f'Current time is: {dt_string}')

def back_button_to_menu_handler(update, context):
    # Create the button
    button1 = InlineKeyboardButton("Personal Center", callback_data="button_1")
    button2 = InlineKeyboardButton("Deposit", callback_data="button_2")
    button3 = InlineKeyboardButton("Withdrawal", callback_data="button_3")
    button4 = InlineKeyboardButton("History", callback_data="button_4")

    # Create the keyboard
    keyboard = [[button1], [button2], [button3], [button4]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send the message with the button
    bot.edit_message_text(chat_id=update.callback_query.message.chat_id, message_id=update.callback_query.message.message_id ,text="Este es un mensaje editado por account", reply_markup=reply_markup)

def main_menu_handler(update, context):
    user_info=update.message
    update.message.reply_text(f'{user_info.from_user.username} este es el menu del boton')
    # Create the button
    button1 = InlineKeyboardButton("Personal Center", callback_data="button_1")
    button2 = InlineKeyboardButton("Deposit", callback_data="button_2")
    button3 = InlineKeyboardButton("Withdrawal", callback_data="button_3")
    button4 = InlineKeyboardButton("History", callback_data="button_4")


    # Create the keyboard
    keyboard = [[button1], [button2], [button3], [button4]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send the message with the button
    bot.send_message(chat_id=update.message.chat_id, text="Press the button:", reply_markup=reply_markup)

def button_handler(update,context):
    query = update.callback_query
    if query.data == "button_1":
        account_information(update)

    elif query.data == "back_account":
        back_button_to_menu_handler(update, context)


    elif query.data == "button_2":
        deposit(update)
    
    elif query.data == "button_3":
        withdrawal(update)

    elif query.data == "button_4":
        history(update)

####### Funciones que se aplican dentro del menu ###########
def account_information(update):
    query = update.callback_query
    query.answer()
    account_information = InlineKeyboardButton("Account Information", callback_data="account")
    wallet = InlineKeyboardButton("Wallet", callback_data='wallet')
    back_personal = InlineKeyboardButton("Back", callback_data='back_account')
    
    keyboard = [[account_information, wallet],[back_personal]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.edit_message_text(chat_id=update.callback_query.message.chat_id, message_id=update.callback_query.message.message_id ,text="This is your personal center, please choose an option by using the buttons below", reply_markup=reply_markup)
    #print(update.callback_query.message.message_id)
    #query.edit_message_text(text="This is your personal center, please choose an option by using the buttons below", reply_markup=reply_markup)
    

def deposit(update):
    query = update.callback_query
    query.answer()
    account_information = InlineKeyboardButton("Deposited", callback_data='deposited')
    wallet = InlineKeyboardButton("Cancel", callback_data='cancel')
    keyboard = [[account_information, wallet]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Minimum deposit amount is $10, to proceed with deposit please send USDT TRC20 to address below \n ```Tjaksdjqiojdlkasjd9182381jksd0X```", reply_markup=reply_markup, parse_mode='Markdown')  

def withdrawal(update):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="Mnimum withdrawal amount is $10, to proceed please send below the wallet to withdraw", parse_mode='Markdown')  

def history(update):
    query = update.callback_query
    query.answer()
    pagina_anterior = InlineKeyboardButton("Pagina anterior", callback_data='anterior')
    pagina_siguiente = InlineKeyboardButton("Pagina siguiente", callback_data='siguiente')
    back_button = InlineKeyboardButton("Back", callback_data='back')
    keyboard = [[pagina_anterior, pagina_siguiente],[back_button]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Estas en el modo historial, aca puedes ver todas las operaciones que has realizado. Usa los botones", reply_markup=reply_markup, parse_mode='Markdown')  


def main():
    t_bot=Bot(api_key)
    updater=Updater(bot=t_bot, use_context=True)
    comando=[("start","Iniciar el bot"),("help","Comandos de bot"),("finalizar","terminar alguna cosa"),("gettime","Obtener el tiempo"),("button", "ensayo del boton")]
    t_bot.set_my_commands(comando)
    dp=updater.dispatcher
    dp.add_handler(MessageHandler(filters=Filters.text & (~Filters.command), callback=message_handler))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_function))
    dp.add_handler(CommandHandler("gettime", get_time))
    dp.add_handler(CommandHandler("menu", main_menu_handler)) 
    updater.dispatcher.add_handler(CallbackQueryHandler(button_handler))     
    updater.start_polling()
    updater.idle()



if __name__=='__main__':
    main()