from django.views import generic
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from .models import Game, Player, Tourney
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def standart(request):
    games = Game.objects.filter(active=True)
    context = {'games': games, 'judgable' : games.filter(judgeable=True)}
    return render(request, 'pixelwars/standart/index.html', context)

def notActiveGameOrNoGame(player):
    games = Game.objects.filter(Q(player1 = player) | Q(player2 = player))
    for game in games:
        if game.active:
            return False

    return True

def readstandart(request, id):
    game = get_object_or_404(Game, id=id)
    players = (game.player1, game.player2)
    canPlay = False
    canJoin = False
    currentPlayer = Player.objects.get(user=request.user)
    #playerCount = Player.objects.filter(game=game)
    if(currentPlayer in players and not currentPlayer.hasDrawed):
        canPlay = True
    if (not currentPlayer in players and notActiveGameOrNoGame(currentPlayer)):
        canJoin = True
    context = {
        'canJoin': canJoin,
        'canPlay': canPlay,
        'currentPlayer': currentPlayer,
        #'playerCount' : playerCount,
        'players': players,
        'game': game,
    }
    return render(request, 'pixelwars/standart/read.html', context)


def index(request):
    return render(request, 'pixelwars/index.html', {'players': Player.objects.order_by('-wins')[:10]})


def tourney(request):
    return render(request, 'pixelwars/tourney/index.html')


def createGame(request):
    if (request.POST['theme'] != ''):
        game = Game()
        game.theme = request.POST['theme']
        player = Player.objects.get(user=request.user)
        game.player1 = player
        game.save()

    return HttpResponseRedirect('/pixelwars/standart/')


def register(request):
    user = User()
    user.username = request.GET['username']
    user.set_password(request.GET['password'])
    user.email = request.GET['email']
    user.first_name = request.GET['name']
    user.last_name = request.GET['pic']
    user.save()
    login(user)
    player = Player(user=user)
    player.name = user.username
    player.save()

    return HttpResponseRedirect('/pixelwars/standart/')


def logIn(request):
    username = request.GET['username']
    password = request.GET['password']
    user = authenticate(username=username, password=password)
    if (user is not None):
        login(request, user)
    return HttpResponseRedirect('/pixelwars/')


def logOut(request):
    logout(request)
    return HttpResponseRedirect('/pixelwars/')


def joinGame(request, id):
    player = Player.objects.get(user=request.user)
    game = Game.objects.get(id=id)
    game.player2 = player
    game.save()
    url = '/pixelwars/standart/' + id + '/'
    return HttpResponseRedirect(url)


def leaveGame(request, id):
    player = Player.objects.get(user=request.user)
    player.hasDrawed = False
    player.game = None
    player.save()
    url = '/pixelwars/standart/' + id + '/'
    return HttpResponseRedirect(url)


def draw(request, id):
    context = {}
    context["gameId"] = id
    return render(request, 'pixelwars/standart/draw.html', context)

@csrf_exempt
def submitDrawing(request, id):
    player = Player.objects.get(user=request.user)
    game = Game.objects.get(id=id)
    player.hasDrawed = True

    drawing = request.POST.get('drawing', 0)
    print(drawing)
    player.drawing = drawing
    player.save()

    return HttpResponseRedirect('/pixelwars/standart/' + id + "/")


def judge(request, id):
    game = Game.objects.get(id=id)
    drawing1 = game.drawing1
    drawing2 = game.drawing2
    print(Game.player_set.all())
    context = {
        'game' : game,
        'drawing1' : drawing1,
        'drawing2' : drawing2,
    }
    return render(request, 'pixelwars/standart/judge.html', context)


def viewUser(request, id):
    user = User.objects.get(id=id)
    context = {
        'username': user.username,
        'email': user.email,
        'name': user.first_name,
        'datejoined': user.date_joined,
    }
    return render(request, 'pixelwars/user/readprofile.html', context)

