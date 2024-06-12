import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fft_bot.settings")
app = Celery("fft_bot_celery_brocker")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()