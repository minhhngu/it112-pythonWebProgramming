from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('games/', views.games, name='game_list'),
    path('gamedetail/<int:id>', views.gameDetail, name='detail'),
    path('gamegenres/', views.gamegenres, name='gamegenre_list'),
    path('gamereviews/', views.gamereviews, name='gamereview_list'),
    path('reviews/<int:id>', views.reviews, name='rev'),
    path('gamestypes/', views.gametypes, name='gametype_list'),
    path('newreview/', views.newreview, name='newreview'),
    path('newgame/', views.newgame, name='newgame'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]
