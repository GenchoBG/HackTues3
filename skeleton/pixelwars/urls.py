from django.conf.urls import url
from . import views

app_name = 'pixelwars'

urlpatterns = [
    #/pixelwars/
    url(r'^$', views.index, name='index'),

    #/pixelwars/standart/
    url(r'standart/$', views.standart, name='standart'),

    #/pixelwars/standart/<id>/
    url(r'standart/(?P<id>\d+)/$', views.readstandart, name='readstandart'),

    #/pixelwars/tourney/
    url(r'tourney/$', views.tourney, name="tourney"),

    #TODO:
    #/pixelwars/tourney/<id>/
    #url(r'tourney/(?P<id>\d+)/$', views.readtourney, name='readtourney'),

    #pixelwars/standart/newgame
    url(r'standart/newgame/$', views.createGame, name='createGame'),

    #pixelwars/register
    url(r'register/$', views.register, name='register'),

    #pixelwars/login
    url(r'login/$', views.logIn, name='login'),

    #pixelwars/logout
    url(r'logout/$', views.logOut, name='logout'),

    # /pixelwars/standart/<id>/join
    url(r'standart/(?P<id>\d+)/join/$', views.joinGame, name='joinGame'),

    # /pixelwars/standart/<id>/leave
    url(r'standart/(?P<id>\d+)/leave/$', views.leaveGame, name='leaveGame'),

    # /pixelwars/user/id/
    url(r'user/(?P<id>\d+)/$', views.viewUser, name='viewUser'),

    # /pixelwars/standart/<id>/draw/
    url(r'standart/(?P<id>\d+)/draw/$', views.draw, name='draw'),

    # /pixelwars/standart/<id>/draw/submit/
    url(r'standart/(?P<id>\d+)/draw/submit/$', views.submitDrawing, name='submitDrawing'),

    # /pixelwars/standart/<id>/judge/
    url(r'standart/(?P<id>\d+)/judge/$', views.judge, name='judge'),
    ]

