import django
import os
import sys

# https://docs.djangoproject.com/en/4.2/topics/settings/#calling-django-setup-is-required-for-standalone-django-usage
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fft_bot.settings")
django.setup()

from telebot import types
from handlers import (
    start_page,
    my_profile_handler,
    find_user_handler,
    change_data_handler,
    info_handler,
    my_friends_handler,
)
from reviews import reviews_message
import text
import re
from config import bot
from gamers.models import Gamers, TeleData
from gamers import tasks
from registration import registrate_email

@bot.message_handler(commands=['start'])
def start_handler(message: types.Message):
    tasks.test_task.delay()
    try:
        gamer = Gamers.objects.get(telegram_id=message.from_user.id)
        start_page(message)
    except Gamers.DoesNotExist as error:
        bot.send_message(message.from_user.id, text='Введіть будь ласка вашу поштову адресу')
        bot.register_next_step_handler(message, registrate_email)

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
