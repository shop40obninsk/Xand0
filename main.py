import telebot
import Sender_message_telegram
import message_worker
import tele_keyboards

with open("token.txt","r") as f:
    token=f.readline().replace("\n",'').replace(" ","")

bot = telebot.TeleBot(token)
print("LAUNCH")
Core=None
User_figure=None
@bot.message_handler(commands=['start'])
def get_text_messages(message):
    keyboard = tele_keyboards.Keyboard_Generator(["/start"])
    Sender_message_telegram.send_message(bot, message, "Крестики нолики", keyboard=keyboard)
    keyboard=tele_keyboards.Inline_Keyboard_Generator([['X','C1'],["0","C0"]],X=[2])
    Sender_message_telegram.send_message(bot,message,"Chose X or 0",keyboard=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def Callback_inline(call):
    global Core
    global User_figure
    if call.message:
        text = str(call.data)
        chat_id = call.message.chat.id
        name = call.message.chat.username
        print("button_inline",text,chat_id)
        Core,User_figure=message_worker.inline_buttons_worker(bot,call,text,Core,User_figure)

bot.polling(none_stop=True, interval=0)