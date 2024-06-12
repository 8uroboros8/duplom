from celery_app import app
from telegram_bot.config import bot

@app.task
def broadcust_of_message(id_arr, text):
    for id in id_arr:
        bot.send_message(chat_id=id, text=text)