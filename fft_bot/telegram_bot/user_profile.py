from telebot import types
from config import bot
import telegram_bot.text as text

from gamers.models import Gamers, TeleData

def user_info(message: types.Message):
    user_photos = bot.get_user_profile_photos(message.from_user.id)
    gamer = Gamers.objects.get(telegram_id=message.from_user.id)
    profile_info = text.Profile_info.format(
        nickname=message.from_user.first_name,
        email=gamer.email,
        user_games=', '.join([game.name for game in gamer.games_set.all()]),
        linc=message.from_user.username,
        # user_about=message.from_user,
    )
    if user_photos.total_count > 0:
        photo_file_id = user_photos.photos[0][0].file_id
        bot.send_photo(message.from_user.id, photo_file_id, caption=profile_info)
    else:
        bot.send_message(message.from_user.id, profile_info)

def find_info(call: types.CallbackQuery, user_state):
    ctx_game_id = user_state[call.from_user.id]['find_in_group']
    ctx_page = user_state[call.from_user.id]['find_in_group_page_index']

    gamers_in_game_group = Gamers.objects.filter(games__id=ctx_game_id)
    gamers_set = gamers_in_game_group.all()
    print(gamers_set)
    # В групі не має користувачів
    if gamers_set.count() < 1:
        bot.send_message(call.from_user.id, 'В цій групі не має користувачів')
        bot.answer_callback_query(call.id)
        return

    # TODO FIXME IndexError: list index out of range
    selected_gamer = gamers_in_game_group.all()[ctx_page]
    user_photos = bot.get_user_profile_photos(selected_gamer.telegram_id)

    inline_markup = types.InlineKeyboardMarkup()
    # if 
    btn_prev = types.InlineKeyboardButton("назад", callback_data="find_in_group_prev")
    btn_page_counter = types.InlineKeyboardButton(f'{ctx_page + 1}/{gamers_set.count()}', callback_data='callback_data')
    btn_next = types.InlineKeyboardButton("наступний", callback_data="find_in_group_next")
    btn_friend = types.InlineKeyboardButton("в друзі", callback_data=f"add_friend_#{selected_gamer.id}")
    inline_markup.add(btn_friend)
    inline_markup.add(btn_prev, btn_page_counter, btn_next)

    selected_gamer_teledata = TeleData.objects.get(telegram_id=selected_gamer.telegram_id)
    profile_check_info = text.Profile_check_info.format(
        nickname=selected_gamer_teledata.telegram_name,
        user_games=', '.join([game.name for game in selected_gamer.games_set.all()]),
        user_about='TODO',
    )
    if user_photos.total_count > 0:
        photo_file_id = user_photos.photos[0][0].file_id
        bot.send_photo(call.from_user.id, photo_file_id, caption=profile_check_info, reply_markup=inline_markup)
    else:
        bot.send_message(call.from_user.id, profile_check_info, reply_markup=inline_markup)

    bot.answer_callback_query(call.id)