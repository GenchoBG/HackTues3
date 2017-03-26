from django.http import JsonResponse
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
    judgeGames = Game.objects.filter(active=True).filter(judgable=True).all()
    games = Game.objects.filter(active=True).filter(judgable=False).all()
    context = {'games': games, 'judgeGames': judgeGames}
    return render(request, 'pixelwars/standart/index.html', context)


def notActiveGameOrNoGame(player):
    games = Game.objects.filter(Q(player1=player) | Q(player2=player))
    for game in games:
        if game.active:
            return False

    return True


def readstandart(request, id):
    game = get_object_or_404(Game, id=id)
    players = []
    if (game.player1 != None):
        players.append(game.player1)
    if (game.player2 != None):
        players.append(game.player2)
    canPlay = False
    canJoin = False
    canLeave = False
    currentPlayer = Player.objects.get(user=request.user)
    if (currentPlayer in players):
        canLeave = True
    playerCount = len(players)
    if (currentPlayer in players and not currentPlayer.hasDrawed):
        canPlay = True
    if (not currentPlayer in players and notActiveGameOrNoGame(currentPlayer)):
        canJoin = True

    context = {
        'canJoin': canJoin,
        'canPlay': canPlay,
        'currentPlayer': currentPlayer,
        'playerCount': playerCount,
        'canLeave': canLeave,
        'players': players,
        'game': game,
    }
    return render(request, 'pixelwars/standart/read.html', context)


def index(request):
    return render(request, 'pixelwars/index.html', {'players': Player.objects.order_by('-wins')[:10]})


def tourney(request):
    return render(request, 'pixelwars/tourney/index.html', {'tourneys': Tourney.objects.all()})


def readtourney(request, id):
    tourney = get_object_or_404(Tourney, id=id)
    canJoin = True
    if ((tourney.player1 and tourney.player1.user == request.user) or (
        tourney.player2 and tourney.player2.user == request.user) or (
        tourney.player3 and tourney.player3.user == request.user) or (
        tourney.player4 and tourney.player4.user == request.user)):
        canJoin = False
    return render(request, 'pixelwars/tourney/read.html', {'tourney': tourney, 'canJoin': canJoin})


def jointourney(request, id):
    tourney = Tourney.objects.get(id=id)
    player = Player.objects.get(user=request.user)
    if not tourney.player1:
        tourney.player1 = player
    elif not tourney.player2:
        tourney.player2 = player
    elif not tourney.player3:
        tourney.player3 = player
    elif not tourney.player4:
        tourney.player4 = player

    tourney.save()
    return HttpResponseRedirect('pixelwars/tourney/' + id + '/')


def leavetourney(request, id):
    tourney = Tourney.objects.get(id=id)
    player = Player.objects.get(user=request.user)
    if (tourney.player1 and tourney.player1.user == request.user):
        tourney.player1 = None
    elif (tourney.player2 and tourney.player2.user == request.user):
        tourney.player2 = None
    elif (tourney.player3 and tourney.player3.user == request.user):
        tourney.player3 = None
    elif (tourney.player4 and tourney.player4.user == request.user):
        tourney.player4 = None

    tourney.save()
    return HttpResponseRedirect('pixelwars/tourney/' + id + '/')


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
    login(request, user)
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
    if not game.player2:
        game.player2 = player
    else:
        game.player1 = player
    game.save()
    url = '/pixelwars/standart/' + id + '/'
    return HttpResponseRedirect(url)


def leaveGame(request, id):
    game = Game.objects.get(id=id)
    if (game.player1 and game.player1.user == request.user):
        player = game.player1
        player.hasDrawed = False
        player.save()
        game.player1 = None
    if (game.player2 and game.player2.user == request.user):
        player = game.player2
        player.hasDrawed = False
        player.save()
        game.player2 = None
    game.save()
    url = '/pixelwars/standart/' + id + '/'
    return HttpResponseRedirect(url)


def draw(request, id):
    context = {}
    context["gameId"] = id
    return render(request, 'pixelwars/standart/draw.html', context)


@csrf_exempt
def submitDrawing(request, id):
    game = Game.objects.get(id=id)
    player = None

    if (game.player1 and game.player1.user == request.user):
        player = game.player1
    if (game.player2 and game.player2.user == request.user):
        player = game.player2

    player.hasDrawed = True
    drawing = request.POST.get('drawing', 0)

    if (game.player1 and game.player1.user == request.user):
        game.drawing1 = drawing
    if (game.player2 and game.player2.user == request.user):
        game.drawing2 = drawing

    player.save()

    if (game.player1 and game.player1.hasDrawed and game.player2 and game.player2.hasDrawed):
        player1 = game.player1
        player1.hasDrawed = False
        player1.save()
        player2 = game.player2
        player2.hasDrawed = False
        player2.save()
        game.judgable = True

    game.save()

    return JsonResponse({"url": '/pixelwars/standart/'})


def judge(request, id):
    game = Game.objects.get(id=id)
    context = {
        'game': game,
        'drawing1': game.drawing1,
        'drawing2': game.drawing2,
        'player1': game.player1,
        'player2': game.player2,
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


def vote1(request, id):
    game = Game.objects.get(id=id)
    player = game.player1
    player.wins += 2
    player.hasDrawed = False
    player.save()
    otherPlayer = game.player2
    otherPlayer.wins -= 1
    otherPlayer.hasDrawed = False
    otherPlayer.save()
    game.active = False
    game.save()
    return HttpResponseRedirect('/')


def vote2(request, id):
    game = Game.objects.get(id=id)
    player = game.player2
    player.wins += 2
    player.hasDrawed = False
    player.save()
    otherPlayer = game.player1
    otherPlayer.wins -= 1
    otherPlayer.hasDrawed = False
    otherPlayer.save()
    game.active = False
    game.save()
    return HttpResponseRedirect('/')

    # LIST judge views
