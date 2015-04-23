from django.conf.urls import patterns, include, url


urlpatterns = (
    patterns(
        'tictactoe.views',
        url(r'^invite$', 'new_invitation', name='invite'),
        url(r'invitation/(?P<pk>\d+)/$', 'accept_invitation', name='invitation'),
        url(r'game/(?P<pk>\d+)/$', 'game_detail', name='detail')
    ))