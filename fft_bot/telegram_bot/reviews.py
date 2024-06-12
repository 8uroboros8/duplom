from telebot import types
from config import bot
from handlers import start_page
import re


def reviews_message(message: types.Message):
    review = message.text
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.add("Відправити")
    markup.add("Скасувати")
    bot.send_message(message.from_user.id, text=f'Ваше повідомлення:\n\n{review}\n\nВідправити?', reply_markup=markup)
    print(f"Review captured: {review}")
    bot.register_next_step_handler(message, validate_reviews_message, review)


def validate_reviews_message(message: types.Message, review):
    print(f"Next step handler triggered with message: {message.text}")
    bot.send_message(message.from_user.id, text=message.text)
    if 'Відправити' in message.text:
        validate_sucsess(message, review)
    elif 'Скасувати' in message.text:
        validate_stop(message)
    else:
        print(message.text)

def validate_sucsess(message, review):
    bot.send_message(chat_id=569220786, text=review)
    bot.send_message(message.from_user.id, text='Повідомлення успішно відправлено')
    return start_page(message)

def validate_stop(message):
    bot.send_message(message.from_user.id, text='Відправку повідомлення сксовано')
    return start_page(message)
