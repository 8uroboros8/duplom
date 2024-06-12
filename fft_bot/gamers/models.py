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
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    telegram_id = models.CharField(max_length=50)
    friend = models.ManyToManyField('self', symmetrical=False, related_name='friends_with')
    
    def __str__(self):
        return self.name


class Games(models.Model):
    name = models.CharField(max_length=50)
    gamers = models.ManyToManyField(to=Gamers)
    
class TeleData(models.Model):
    telegram_id = models.IntegerField(blank=False)
    telegram_photo = models.IntegerField(blank=True)
    telegram_name = models.CharField(max_length=50)
    telegram_link = models.CharField(max_length=50)
    