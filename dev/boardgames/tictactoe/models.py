from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Game(models.Model):
  first_player = models.ForeignKey(User, related_name="games_first_player")
  second_player = models.ForeignKey(User, related_name="games_second_player")
  next_to_move = models.ForeignKey(User, related_name="game_to_move")
  start_time = models.DateTimeField(auto_now_add=True)
  last_active = models.DateTimeField(auto_now=True)


class Move(models.Model):
  """Represents a TicTacToe player movement"""
  x = models.IntegerField()
  y = models.IntegerField()
  comment = models.CharField(max_length=300)
  game = models.ForeignKey(Game)