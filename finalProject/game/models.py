from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class GameType(models.Model):
    gameconsole = models.CharField(max_length=255)

    def __str__(self):
        return self.gameconsole

    class Meta:
        db_table = 'gametype'
        verbose_name_plural = 'gametypes'


class GameGenre(models.Model):
    typegenre = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.typegenre

    class Meta:
        db_table = 'gamegenre'
        verbose_name_plural = 'gamegenres'


class Game(models.Model):
    gamename = models.CharField(max_length=255)
    gametype = models.ForeignKey(GameType, on_delete=models.DO_NOTHING)
    gamegenre = models.ForeignKey(GameGenre, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    gameurl = models.URLField(null=True, blank=True)
    gamedescription = models.TextField()

    def __str__(self):
        return self.gamename

    class Meta:
        db_table = 'game'
        verbose_name_plural = 'games'


class GameReview(models.Model):
    reviewtitle = models.CharField(max_length=255)
    reviewdate = models.DateField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ManyToManyField(User)
    reviewrating = models.SmallIntegerField()
    reviewtext = models.TextField()

    def __str__(self):
        return self.reviewtitle

    class Meta:
        db_table = 'gamereview'
        verbose_name_plural = 'gamereviews'
