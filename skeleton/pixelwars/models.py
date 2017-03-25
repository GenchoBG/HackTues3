from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Game(models.Model):
    theme = models.CharField(max_length=100, null=1)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.theme

class Player(models.Model):
    name = models.CharField(max_length=250, null=1)
    game = models.ForeignKey(Game, null=1)
    user = models.OneToOneField(User, null=1, unique=True)
    wins = models.IntegerField(default=0)
    hasDrawed = models.BooleanField(default=False)
    #drawing
    def __str__(self):
        return self.name

class Tourney(models.Model):
    name = models.CharField(max_length=250, null=1)