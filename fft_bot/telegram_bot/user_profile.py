import telebot
from telebot import types
from config import bot
import text as text

def user_info(message: types.Message):
    user_photos = bot.get_user_profile_photos(message.from_user.id)

    if user_photos.total_count > 0:
        photo_file_id = user_photos.photos[0][0].file_id
        bot.send_photo(message.from_user.id, photo_file_id, caption=text.Profile_info)
    else:
        bot.send_message(message.from_user.id, text.Profile_info)

def find_info(message: types.Message):
    user_photos = bot.get_user_profile_photos(message.from_user.id)
    inline_markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("назад", callback_data="back")
    btn2 = types.InlineKeyboardButton("в друзі", callback_data="add_friend")
    btn3 = types.InlineKeyboardButton("наступний", callback_data="next")
    inline_markup.add(btn1, btn2, btn3)
    if user_photos.total_count > 0:
        photo_file_id = user_photos.photos[0][0].file_id
        bot.send_photo(message.from_user.id, photo_file_id, caption=text.Profile_check_info, reply_markup=inline_markup)
    else:
        bot.send_message(message.from_user.id, text.Profile_check_info, reply_markup=inline_markup)