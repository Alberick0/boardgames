from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import InvitationForm
from .models import Invitation


@login_required()
def new_invitation(request):
    if request.method == 'POST':
        invitation = Invitation(from_user=request.user)
        form = InvitationForm(data=request.POST, instance=invitation)

        if form.is_valid():
            form.save()
            return redirect('user_home')

    else:
        form = InvitationForm()

    return render(request, 'tictactoe/new_invitation.html', {'form': form})
