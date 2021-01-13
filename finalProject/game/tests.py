from django.test import TestCase
from .models import Game, GameGenre, GameType, GameReview
from django.contrib.auth.models import User
from .forms import GameForm, ReviewForm
import datetime
from django.urls import reverse_lazy, reverse

# Create your tests here.


class GameTypeTest(TestCase):
    def setUp(self):
        self.type = GameType(gameconsole='PlayStation 4')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'PlayStation 4')

    def test_tablename(self):
        self.assertEqual(str(GameType._meta.db_table), 'gametype')


class GameGenreTest(TestCase):
    def setUp(self):
        self.type = GameGenre(typegenre='Action-Adventure RPG')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'Action-Adventure RPG')

    def test_tablename(self):
        self.assertEqual(str(GameGenre._meta.db_table), 'gamegenre')


class GameTest(TestCase):
    def setUp(self):
        self.type = Game(gamename='God of War')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'God of War')

    def test_tablename(self):
        self.assertEqual(str(Game._meta.db_table), 'game')


class GameReviewTest(TestCase):
    def setUp(self):
        self.type = GameReview(reviewtitle='God of War Review')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'God of War Review')

    def test_tablename(self):
        self.assertEqual(str(GameReview._meta.db_table), 'gamereview')


class NewGameForm(TestCase):
    def test_gameform(self):
        data = {
            'gamename': 'God of War',
            'user': 'minh',
            'gameurl': 'http://godofwar.com',
            'gamedescription': 'Based in ancient mythology, the story follows Kratos, a Spartan warrior who was tricked into killing his family by his former master, the Greek God of War Ares. This sets off a series of events that leads to wars with the mythological pantheons.',
        }

        form = GameForm(data)
        self.assertTrue(form.is_valid)


class New_Game_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username='testuser1', password='P@ssw0rd1')
        self.gametype = GameType.objects.create(gameconsole='PlayStation 4')
        self.game = Game(
            gamename='God of War',
            user=self.test_user,
            gameurl='http://godofwar.com',
            gamedescription='Based in ancient mythology, the story follows Kratos, a Spartan warrior who was tricked into killing his family by his former master, the Greek God of War Ares. This sets off a series of events that leads to wars with the mythological pantheons.',
        )

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('newgame'))
        self.assertRedirects(
            response, '/accounts/login/?next=/game/newgame/')


class NewReviewForm(TestCase):
    def test_reviewform(self):
        data = {
            'reviewtitle': 'God of War Review',
            'reviewdate': '2020-01-13',
            'user': 'minh',
            'reviewrating': '10',
            'reviewtext': 'Best game on the PS4!',
        }

        form = GameForm(data)
        self.assertTrue(form.is_valid)


class New_GameReview_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username='testuser1', password='P@ssw0rd1')
        self.gamereview = GameReview(
            reviewtitle='God of War Review',
            reviewdate=datetime.date(2021, 1, 13),
            reviewrating=10,
            reviewtext='Best game on the PS4!',
        )

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('newreview'))
        self.assertRedirects(
            response, '/accounts/login/?next=/game/newreview/')
