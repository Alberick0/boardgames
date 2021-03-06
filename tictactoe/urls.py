from django.conf.urls import patterns, include, url

from .views import AllGamesList


urlpatterns = (
    patterns(
        'tictactoe.views',
        url(r'^invite$', 'new_invitation', name='invite'),
        url(r'invitation/(?P<pk>\d+)/$', 'accept_invitation', name='invitation'),
        url(r'game/(?P<pk>\d+)/$', 'game_detail', name='detail'),
        url(r'game/(?P<pk>\d+)/move$', 'game_do_move', name='move'),
        url(r'game/all$', AllGamesList.as_view(), name='move'),
    ))