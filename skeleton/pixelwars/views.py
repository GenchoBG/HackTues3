from django.views import generic
from django.http import HttpResponseRedirect
from .models import Game, Player, Tourney
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def standart(request):
    games = Game.objects.filter(active=True)
    context = {'games': games}
    return render(request, 'pixelwars/standart/index.html', context)


def readstandart(request, id):
    # game = Game.objects.get(id=id)
    game = get_object_or_404(Game, id=id)
    players = Player.objects.filter(game=game)
    flag = False


    try:
        currentPlayer = Player.objects.filter(user=request.user).filter(game=game).get()
    except:
        currentPlayer = Player.objects.filter(user=request.user).filter(game=game)

    playerCount = players.count()
    canPlay = False
    for player in players:
        if (player.user.id == request.user.id):
            if player.hasDrawed == False:
                canPlay = True
            break

    canJoin = True
    try:
        player = Player.objects.filter(user=request.user).get()
        if (player.game != None):
            canJoin = False
    except:
        pass

    context = {
        'canJoin': canJoin,
        'canPlay': canPlay,
        'playerCount': playerCount,
        'currentPlayer': currentPlayer,
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
        game.save()
        user = request.user
        player = Player()
        player.name = user.username
        player.user = user
        player.game = game
        player.save()

    return HttpResponseRedirect('/pixelwars/standart/')


def register(request):
    user = User()
    user.username = request.GET['username']
    user.set_password(request.GET['password'])
    user.email = request.GET['email']
    user.first_name = request.GET['name']
    user.last_name = request.GET['pic']
    user.save()
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
    if (not Player.objects.get(user=request.user)):
        player = Player()
        player.user = request.user
        player.name = request.user.username
    else:
        player = Player.objects.get(user=request.user)
    player.game = Game.objects.get(id=id)
    player.save()
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
    player = Player.objects.get(user=request.user)
    player.hasDrawed = True
    player.save()
    return HttpResponseRedirect('/pixelwars/standart/' + id + "/")


def judge(request, id):
    pass


def viewUser(request, id):
    user = User.objects.get(id=id)
    context = {
        'picture': user.last_name,
        'username': user.username,
        'email': user.email,
        'name': user.first_name,
        'datejoined': user.date_joined,
    }
    return render(request, 'pixelwars/user/readprofile.html', context)
