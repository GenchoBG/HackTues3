from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Game(models.Model):
    theme = models.CharField(max_length=100, null=True)
    active = models.BooleanField(default=True)
    drawing1 = models.ImageField(null=True)
    drawing2 = models.ImageField(null=True)

    def __str__(self):
        return self.theme


class Player(models.Model):
    name = models.CharField(max_length=250, null=True)
    game = models.ForeignKey(Game, null=True)
    user = models.OneToOneField(User, null=True, unique=True)
    wins = models.IntegerField(default=0)
    hasDrawed = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Tourney(models.Model):
    name = models.CharField(max_length=250, null=True)
