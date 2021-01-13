from django.contrib import admin
from .models import GameType, GameGenre, Game, GameReview

# Register your models here.
admin.site.register(GameType)
admin.site.register(GameGenre)
admin.site.register(Game)
admin.site.register(GameReview)
