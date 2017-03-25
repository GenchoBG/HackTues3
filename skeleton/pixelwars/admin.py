from django.contrib import admin
from .models import Game
from .models import Player
from .models import Tourney

# Register your models here.

admin.site.register(Game)
admin.site.register(Player)
admin.site.register(Tourney)
