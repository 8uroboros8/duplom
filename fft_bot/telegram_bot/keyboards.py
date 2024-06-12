import telebot
from telebot import types
import emoji


class Keyboard():
    main_menu_button = emoji.emojize(":left_arrow: Головне меню")

    def __init__(self, bot):
        self.bot = bot

    def _get_start_markup(self):
        start_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        start_markup.row(emoji.emojize(":beer_mug: Мій профіль"), emoji.emojize(":beating_heart: Мої друзі"))
        start_markup.row(emoji.emojize(":magnifying_glass_tilted_right: Розпочати пошук"), emoji.emojize(":clipboard: Змінити мої дані"))
        start_markup.row(emoji.emojize(":loudspeaker: Відгуки/Скарги/Пропозиції"), emoji.emojize(f":information: Про бота"))
        return start_markup

    def start_menu(self, message, content):
        self.bot.send_message(message.from_user.id, content, reply_markup=self._get_start_markup())
