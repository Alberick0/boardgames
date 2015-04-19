from django.db import models
from django.contrib.auth.models import User


STATUS_CHOICES = (
    ('A', 'Active'),
    ('F', 'First'),
    ('S', 'Second'),
    ('D', 'Draw'),
)


class Game(models.Model):
    first_player = models.ForeignKey(User, related_name='games_first_player')
    second_player = models.ForeignKey(User, related_name='games_second_player')
    next_to_move = models.ForeignKey(User, related_name='games_to_move')
    start_time = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, default='A', choices=STATUS_CHOICES)

    def __str__(self):
        return '{} vs {}'.format(self.first_player, self.second_player)


class Move(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    comment = models.CharField(max_length=150)
    game = models.ForeignKey(Game)