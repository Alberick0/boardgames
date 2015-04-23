from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q


STATUS_CHOICES = (
    ('A', 'Active'),
    ('F', 'First'),
    ('S', 'Second'),
    ('D', 'Draw'),
)


class GamesManager(models.Manager):  # Custom manager class, which represents the whole table
    def games_for_user(self, user):
        """
        Return a queryset of games that this user participates in
        """

        return super(GamesManager, self).get_queryset().filter(
            Q(first_player_id=user.id) | Q(second_player_id=user.id)
        )  # this query returns all games where the user is either 1stP or 2ndP


class Game(models.Model):
    first_player = models.ForeignKey(User, related_name='games_first_player')
    second_player = models.ForeignKey(User, related_name='games_second_player')
    next_to_move = models.ForeignKey(User, related_name='games_to_move')
    start_time = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, default='A', choices=STATUS_CHOICES)
    objects = GamesManager()  # sets a new manager for this class.

    def __str__(self):
        return '{} vs {}'.format(self.first_player, self.second_player)


class Move(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    comment = models.CharField(max_length=150)
    game = models.ForeignKey(Game)

    def __str__(self):
        return 'Next to move is {}'.format(self.game.next_to_move)


class Invitation(models.Model):
    from_user = models.ForeignKey(User, related_name='invitations_sent')
    to_user = models.ForeignKey(User, related_name='invitations_received', verbose_name='User to invite',
                                help_text='Select the user with who you want to play')
    message = models.CharField('Optional Message', max_length=200, blank=True,
                               help_text='Add a friendly message if you want')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Invitation from {}'.format(self.from_user)