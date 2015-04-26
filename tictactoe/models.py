from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q


STATUS_CHOICES = (
    ('A', 'Active'),
    ('F', 'First'),
    ('S', 'Second'),
    ('D', 'Draw'),
)

FIRST_PLAYER_MOVE = 'X'
SECOND_PLAYER_MOVE = 'O'
BOARD_SIZE = 3


class GamesManager(models.Manager):  # Custom manager class, which represents the whole table
    def games_for_user(self, user):
        """
        Return a queryset of games that this user participates in
        """

        return super(GamesManager, self).get_queryset().filter(
            Q(first_player_id=user.id) | Q(second_player_id=user.id)
        )  # this query returns all games where the user is either 1stP or 2ndP

    def new_game(self, invitation):
        game = Game(first_player=invitation.to_user,
                    second_player=invitation.from_user,
                    next_to_move=invitation.to_user)

        return game


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

    def get_absolute_url(self):
        return reverse('', args=[self.id])

    def last_move(self):
        return self.move_set.latest()  # latest is defined by django it will use the get_latest_by field

    def is_users_move(self, user):
        return self.status == 'A' and self.next_to_move == user

    def as_board(self):
        """
        Return a representation of the game board as two-dimensional list,
        so you can ask for the state of a square position [y][x].

        It will contain a list of lines, where every line is a list of 'X', 'O' or ''.
        For example a 3x3 board position:

        [['', 'X', ''],
         ['O', '', ''],
         ['X', '', '']]
        """

        board = [['' for x in range(BOARD_SIZE)] for y in range(BOARD_SIZE)]
        for move in self.move_set.all():
            board[move.y][move.x] = FIRST_PLAYER_MOVE if move.by_first_player else SECOND_PLAYER_MOVE

        return board


class Move(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    comment = models.CharField(max_length=150)
    game = models.ForeignKey(Game)
    by_first_player = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return 'Next to move is {}'.format(self.game.next_to_move)

    class Meta:  # Can be used to add extra options
        get_latest_by = 'timestamp' # tells django what field to look to determinate the latest move

    def player(self):
        return self.game.first_player if self.by_first_player else self.game.second_player


class Invitation(models.Model):
    from_user = models.ForeignKey(User, related_name='invitations_sent')
    to_user = models.ForeignKey(User, related_name='invitations_received', verbose_name='User to invite',
                                help_text='Select the user with who you want to play')
    message = models.CharField('Optional Message', max_length=200, blank=True,
                               help_text='Add a friendly message if you want')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Invitation from {}'.format(self.from_user)