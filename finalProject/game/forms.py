from django import forms
from .models import GameType, GameReview, GameGenre, Game


class ReviewForm(forms.ModelForm):
    class Meta:
        model = GameReview
        fields = '__all__'


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'
