#https://api.telegram.org/bot6259775919:AAGS1aCvDUk9vCiqlBbDN6j2xdISZbNud2Q/getUpdates
#6259775919:AAGS1aCvDUk9vCiqlBbDN6j2xdISZbNud2Q
#Chatid: -815826376
#https://api.telegram.org/bot6259775919:AAGS1aCvDUk9vCiqlBbDN6j2xdISZbNud2Q/sendMessage?chat_id=-815826376&text=test message from python api

from telegram import Update,Bot
from telegram.ext import Updater,MessageHandler,Filters, CommandHandler
from telegram.utils.request import Request
import requests, json
from datetime import datetime

api_key = "6259775919:AAGS1aCvDUk9vCiqlBbDN6j2xdISZbNud2Q"
url="https://api.telegram.org/bot6259775919:AAGS1aCvDUk9vCiqlBbDN6j2xdISZbNud2Q/setMyCommands?commands="

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
comando=[("start","descripcion del inicio"),("help","pedir ayuda"),("finalizar","terminar alguna cosa"),("gettime","Obtener el tiempo")]

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
    update.message.reply_text("Respuesta automatica para fotos")   

def get_time(update, context):
    print(update.message.text)
    now=datetime.now()
    dt_string=now.strftime("%d/%m/%y_%H:%M:%S")
    update.message.reply_text(f'Current time is: {dt_string}')
    print(comando)

def main():
    t_bot=Bot(api_key)
    update=Updater(bot=t_bot, use_context=True)
    comando=[("start","descripcion del inicio"),("help","pedir ayuda"),("finalizar","terminar alguna cosa"),("gettime","Obtener el tiempo")]
    t_bot.set_my_commands(comando)
    dp=update.dispatcher
    dp.add_handler(MessageHandler(filters=Filters.text & (~Filters.command), callback=message_handler))
    dp.add_handler(MessageHandler(filters=Filters.photo, callback=photo_handler))
    dp.add_handler(CommandHandler("gettime", get_time))
    update.start_polling()
    update.idle()

if __name__=='__main__':
    main()