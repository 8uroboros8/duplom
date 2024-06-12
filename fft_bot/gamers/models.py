from django.db import models
# from gamers.models import Gamers, Games
# gamer = Gamers.objects.all()[0] 
# games = Games.objects.all()[0] 
# from pprint import pprint
# pprint(dir(gamer))
# gamer.friends_with
# >>> gamer.friends_with.all()
# >>> gamer.friends_with.add(Gamers.objects.all()[1])  
# >>> gamer.friends_with.all()

class Gamers(models.Model):
    class Meta:
        verbose_name = 'Ігроки'
        verbose_name_plural = verbose_name

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    telegram_id = models.CharField(max_length=50)
    friend = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='friends_with',
        blank=True,
    )

    def __str__(self):
        return self.name


class Games(models.Model):
    class Meta:
        verbose_name = 'Ігри'
        verbose_name_plural = verbose_name

    name = models.CharField(max_length=50)
    gamers = models.ManyToManyField(to=Gamers, blank=True)

    def __str__(self):
        return self.name


class TeleData(models.Model):
    class Meta:
        verbose_name = 'Дані з телеграм'
        verbose_name_plural = verbose_name

    telegram_id = models.IntegerField(blank=False)
    telegram_photo = models.IntegerField(blank=True)
    telegram_name = models.CharField(max_length=50)
    telegram_link = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.telegram_link} ({self.telegram_id})'
