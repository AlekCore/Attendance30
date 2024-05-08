import matplotlib
import telebot
import time

TOKEN = "6856447846:AAGgqkGS36OFJ1jkNUo1_0qnfxsGGPaEUhU"
bot = telebot.TeleBot(TOKEN)
pulh = 18
pulmin = 49

@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"...")
  f = 0
  while True:                                                                            	
    dow, month, day, tim, year = time.ctime().split()
    if int(tim[0:2]) == pulh and int(tim[3:5]) == pulmin and int(tim[6:8]) == 0 and f == 0:
      bot.send_poll(message.chat.id, "In School?", ["YES", "NO"], False)
      f = 1
    if int(tim[0:2]) > pulh:
      f = 0

bot.infinity_polling()
