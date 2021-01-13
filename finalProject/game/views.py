from django.shortcuts import render, get_object_or_404
from .models import GameGenre, Game, GameReview, GameType
from .forms import ReviewForm, GameForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render(request, 'game/index.html')


def games(request):
    game_list = Game.objects.all()
    return render(request, 'game/games.html', {'game_list': game_list})


def gameDetail(request, id):
    game = get_object_or_404(Game, pk=id)
    return render(request, 'game/gamedetail.html', {'game': game})


def gamegenres(request):
    gamegenre_list = GameGenre.objects.all()
    return render(request, 'game/gamegenres.html', {'gamegenre_list': gamegenre_list})


def gamereviews(request):
    gamereview_list = GameReview.objects.all()
    return render(request, 'game/gamereviews.html', {'gamereview_list': gamereview_list})


def reviews(request, id):
    review = get_object_or_404(GameReview, pk=id)
    return render(request, 'game/reviews.html', {'review': review})


def gametypes(request):
    gametype_list = GameType.objects.all()
    return render(request, 'game/gametypes.html', {'gametype_list': gametype_list})


@login_required
def newreview(request):
    form = ReviewForm

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form. is_valid():
            post = form.save(commit=True)
            post.save()
            form = ReviewForm()
    else:
        form = ReviewForm()
    return render(request, 'game/newreview.html', {'form': form})


@login_required
def newgame(request):
    form = GameForm

    if request.method == 'POST':
        form = GameForm(request.POST)
        if form. is_valid():
            post = form.save(commit=True)
            post.save()
            form = GameForm()
    else:
        form = GameForm()
    return render(request, 'game/newgame.html', {'form': form})


def loginmessage(request):
    return render(request, 'game/loginmessage.html')


def logoutmessage(request):
    return render(request, 'game/logoutmessage.html')
