
import logging
from keyboards import Keyboard
from config import bot
import text as text
from user_profile import user_info, find_info
# from reviews import reviews_message
import telebot
from telebot import types

# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# logger = logging.getLogger(__name__)


def get_keyboard(user_id):
    user_position = Keyboard(bot)
    return user_position


def start_page(message):
    user_position = get_keyboard(message.from_user.id)

    content = text.Start_message
    user_position.start_menu(message, content)

def my_profile_handler(message):
    user_info(message)

def my_friends_handler(message):
    bot.send_message(message.chat.id, "На жаль, зараз ваш список порожній, але це можна виправити, просто натисніть \"Розпочати пошук\"")

def send_inline_keyboard(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Дота2", callback_data='game_Dota2')
    btn2 = types.InlineKeyboardButton("CS2", callback_data='game_CS2')
    btn3 = types.InlineKeyboardButton("ESO", callback_data='game_ESO')
    btn4 = types.InlineKeyboardButton("APEX", callback_data='game_APEX')
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.from_user.id, "Виберіть гру для пошуку:", reply_markup=markup)

def find_user_handler(message):
    find_info(message)

def change_data_handler(message):
    change_data_keyboard(message)

def change_data_keyboard(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton("Про мене")
    btn2 = types.KeyboardButton("Назва профілю")
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, "Звичайно", reply_markup=markup)
    change_data2(message)

def change_data2(message: types.Message):
    text = message.text
    print(text)
    if "📋 Змінити мої дані" in text:
        bot.send_message(message.from_user.id, text="Виберіть дані які хочете змінити:")
        reg1(message)
    elif text == "Назва профілю":
        bot.send_message(message.from_user.id, text="Ведіть оновлені дані")

def reg1(message):
    print(message.text)
    if "Про мене" in message.text:
        bot.send_message(message.from_user.id, 'Введіть нові дані')

# def reviews_handler(message):
#     print('222')
#     bot.send_message(message.from_user.id, text=text.Review_text)
#     print('333')
#     bot.register_next_step_handler(message, reviews_message)
    
    
# def reviews_message1(message):
#     bot.send_message(message.from_user.id, text=message.text)
#     bot.register_next_step_handler(message, reviews_message2)
    
# def reviews_message2(message):
#     bot.send_message(message.from_user.id, text=message.text)
#     bot.register_next_step_handler(message, reviews_message3)
    
# def reviews_message3(message):
#     bot.send_message(message.from_user.id, text=message.text)

def info_handler(message):
    bot.send_message(message.from_user.id, text=text.Bot_info)