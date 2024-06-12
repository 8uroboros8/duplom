from telebot import types
from config import bot
import telegram_bot.text as text

from gamers.models import Gamers

def user_info(message: types.Message):
    user_photos = bot.get_user_profile_photos(message.from_user.id)
    gamer = Gamers.objects.get(telegram_id=message.from_user.id)
    profile_info = text.Profile_info.format(
        nickname=message.from_user.username,
        email=gamer.email,
        user_games=', '.join([game.name for game in gamer.games_set.all()]),
        finded_gamers='TODO',
        user_about='TODO',
    )
    if user_photos.total_count > 0:
        photo_file_id = user_photos.photos[0][0].file_id
        bot.send_photo(message.from_user.id, photo_file_id, caption=profile_info)
    else:
        bot.send_message(message.from_user.id, profile_info)

def find_info(message: types.Message):
    user_photos = bot.get_user_profile_photos(message.from_user.id)
    inline_markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("назад", callback_data="back")
    btn2 = types.InlineKeyboardButton("в друзі", callback_data="add_friend")
    btn3 = types.InlineKeyboardButton("наступний", callback_data="next")
    inline_markup.add(btn1, btn2, btn3)

    gamer = Gamers.objects.get(telegram_id=message.from_user.id)
    profile_check_info = text.Profile_check_info.format(
        nickname=message.from_user.username,
        user_games=', '.join([game.name for game in gamer.games_set.all()]),
        user_about='TODO',
    )
    if user_photos.total_count > 0:
        photo_file_id = user_photos.photos[0][0].file_id
        bot.send_photo(message.from_user.id, photo_file_id, caption=profile_check_info, reply_markup=inline_markup)
    else:
        bot.send_message(message.from_user.id, profile_check_info, reply_markup=inline_markup)