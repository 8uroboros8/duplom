from gamers.models import Gamers, TeleData, Games
from telebot import types
from config import bot
from handlers import start_page

def games_markup_func(message):
    gamer = Gamers.objects.get(telegram_id=message.from_user.id)
    gamers_games = gamer.games_set.all()
    all_games = Games.objects.all()
    remaining_games = all_games.exclude(id__in=gamers_games.values('id'))
    games_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for game in remaining_games:
        games_markup.add(game.name)
    games_markup.add("Завершити")
    bot.send_message(message.from_user.id, text='Якщо це все натисніть Завершити', reply_markup=games_markup)

@bot.message_handler(func=lambda message: message.text in ["Dota2", "CS2", "APEX", "TESO", "Завершити"])
def handle_game_selection(message):
    try:
        gamer = Gamers.objects.get(telegram_id=message.from_user.id)
        if message.text == "Dota2":
            game = Games.objects.get(name='Dota2')
            gamer.games_set.add(game)
            games_markup_func(message)
        elif message.text == "CS2":
            game = Games.objects.get(name='CS2')
            gamer.games_set.add(game) 
            games_markup_func(message)
        elif message.text == "APEX":
            game = Games.objects.get(name='APEX')
            gamer.games_set.add(game) 
            games_markup_func(message)
        elif message.text == "TESO":
            game = Games.objects.get(name='TESO')
            gamer.games_set.add(game) 
            games_markup_func(message)
        elif message.text == "Завершити":
            return start_page(message)
    except Gamers.DoesNotExist:
        print('shit')
        return start_page(message)

def registrate_email(message):
    print(message.text)
    Gamers.objects.create(
            name=message.from_user.username,
            email=message.text,
            telegram_id=message.from_user.id,
        )
    TeleData.objects.create(
            telegram_id=message.from_user.id,
            telegram_name=message.from_user.username,
            telegram_link=message.from_user.username,
        )
    
    # markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.from_user.id, "Виберіть гру для пошуку:")
    games_markup_func(message)