from django.conf.urls import patterns, include, url


urlpatterns = [
    url(r'^invite$', 'tictactoe.views.new_invitation', name='invite')
]