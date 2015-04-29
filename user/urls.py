from django.conf.urls import patterns, url

from .views import SingUpView

urlpatterns = patterns(
    'user.views',
    url(r'^home$', 'home', name='user_home'),
    url(r'^signup$', SingUpView.as_view(), name='user_signup'),
)