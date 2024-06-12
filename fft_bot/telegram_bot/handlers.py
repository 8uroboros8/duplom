
import logging
from gamers.models import Gamers
from keyboards import Keyboard
from config import bot
import text as text
from user_profile import user_info, find_info
# from reviews import reviews_message
from telebot import types
from typing import Dict
from gamers.models import Gamers
from gamers.tasks import broadcust_of_message
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# logger = logging.getLogger(__name__)
user_data = {}


@bot.message_handler(func=lambda message: message.text in ["Надіслати", "Відмінити"])
def handle_game_selection(message):
    id_arr = []
    if message.text == "Надіслати":
        all_gamers = Gamers.objects.all()
        text = user_data[message.from_user.id]['text']
        for gamer in all_gamers:
            id_arr.append(gamer.telegram_id)
        print(id_arr)
        broadcust_of_message.delay(id_arr, text)
        return start_page(message)
    elif message.text == "Відмінити":
        return start_page(message)
            
            
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


user_state: Dict[str, dict] = {}


@bot.callback_query_handler(func=lambda call: call.data.startswith('find_in_group_#'))
def find_user_handler(call: types.CallbackQuery):
    game_id = call.data.split('#')[1]

    if not call.from_user.id in user_state:
        user_state[call.from_user.id] = {}

    user_state[call.from_user.id]['find_in_group'] = game_id
    user_state[call.from_user.id]['find_in_group_page_index'] = 0
    find_info(call, user_state)


@bot.callback_query_handler(func=lambda call: call.data.startswith('find_in_group_next'))
def find_user_handler_next(call: types.CallbackQuery):
    user_state[call.from_user.id]['find_in_group_page_index'] += 1
    find_info(call, user_state)


@bot.callback_query_handler(func=lambda call: call.data.startswith('find_in_group_prev'))
def find_user_handler_prev(call: types.CallbackQuery):
    user_state[call.from_user.id]['find_in_group_page_index'] -= 1
    find_info(call, user_state)


def change_data_handler(message):
    broadcust_keyboard(message)

def broadcust_keyboard(message):
    bot.send_message(message.from_user.id, "Введіть ваше повідомлення")
    bot.register_next_step_handler(message, change_data2)

def change_data2(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton("Надіслати")
    btn2 = types.KeyboardButton("Відмінити")
    markup.add(btn1, btn2)
    text = message.text
    if not message.from_user.id in user_data:
        user_data[message.from_user.id] = {}
    user_data[message.from_user.id]['text']=text
    bot.send_message(message.from_user.id, text=f'Збираєтесь надіслати: {text}', reply_markup=markup)
    print(text)
    
    if "Надіслати" in message.text:
        for gamer in all_gamers:
            tele_id = gamer.telegram_id
            broadcust_of_message.delay(message, tele_id, text)
        return start_page(message)
    elif "Відмінити" in message.text:
        return start_page(message)

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