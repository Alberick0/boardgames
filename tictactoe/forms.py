from django.forms import ModelForm
from .models import Invitation, Move


class InvitationForm(ModelForm):
    class Meta:
        model = Invitation
        exclude = ['timestamp', 'from_user']


class MoveForm(ModelForm):
    class Meta:
        model = Move
        exclude = ['game', 'by_first_player', 'comment']