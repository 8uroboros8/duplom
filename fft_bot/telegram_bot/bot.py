import telebot
from telebot import types
from handlers import *
from reviews import reviews_message
import text as text
import re
# from gamers.models import Gamers
API_TOKEN = '6451225634:AAHnwDtRvvhiqlEQI-HXOEsgrUh1tTglQvw'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start_handler(message: types.Message):
    # gamer = Gamers.objects.all()
    # print(gamer.telegram_id)
    start_page(message)

@bot.message_handler(func=lambda message: re.search(r'Відгуки|Скарги|Пропозиції', message.text, re.IGNORECASE))
def reviews_filter(message):
    bot.send_message(message.from_user.id, text=text.Review_text)
    bot.register_next_step_handler(message, reviews_message)

@bot.message_handler(func=lambda message: re.search(r'Мій профіль', message.text, re.IGNORECASE))
def my_profile_filter(message):
    my_profile_handler(message)

@bot.message_handler(func=lambda message: re.search(r'Розпочати пошук', message.text, re.IGNORECASE))
def find_user_filter(message):
    find_user_handler(message)

@bot.message_handler(func=lambda message: re.search(r'Змінити мої дані', message.text, re.IGNORECASE))
def change_data_filter(message):
    change_data_handler(message)


@bot.message_handler(func=lambda message: re.search(r'Про бота', message.text, re.IGNORECASE))
def info_filter(message):
    info_handler(message)

@bot.message_handler(func=lambda message: re.search(r'Мої друзі', message.text, re.IGNORECASE))
def my_friends_filter(message):
    my_friends_handler(message)

    
bot.infinity_polling(none_stop=True)