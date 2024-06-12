import telebot
from telebot import types

API_TOKEN = '6451225634:AAHnwDtRvvhiqlEQI-HXOEsgrUh1tTglQvw'

bot = telebot.TeleBot(API_TOKEN)

# Початковий обробник /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Вітаю! Введіть ваше повідомлення для відгуків:")
    bot.register_next_step_handler(message, reviews_message)

# Обробник для отримання відгуків
def reviews_message(message):
    user_feedback = message.text
    bot.send_message(message.chat.id, f"Дякую за ваш відгук: {user_feedback}")

# Запуск бота
bot.polling()