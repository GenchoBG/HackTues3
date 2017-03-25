from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class Player(models.Model):
    user = models.OneToOneField(User, null=True, unique=True)
    name = models.CharField(max_length=250, null=True)
    wins = models.IntegerField(default=0)
    hasDrawed = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Game(models.Model):
    theme = models.CharField(max_length=100, null=True)
    active = models.BooleanField(default=True)
    drawing1 = models.ImageField(null=True, upload_to="gallery/")
    drawing2 = models.ImageField(null=True, upload_to="gallery/"    )
    player1 = models.ForeignKey(Player, null=True, related_name="player1")
    player2 = models.ForeignKey(Player, null=True, related_name="player2")
    judgable = models.BooleanField(default=False)

    def __str__(self):
        return self.theme


class Tourney(models.Model):
    name = models.CharField(max_length=250, null=True)
