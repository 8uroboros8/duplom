# Запуск
## Адмін-панель
```
py fft_bot/manage.py runserver
```

## Телеграм бот
```
py fft_bot/telegram_bot/bot.py
```

## Брокер повідомлень
```
celery -A celery_app worker --pool=solo
```
