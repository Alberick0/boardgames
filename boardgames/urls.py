from django.conf.urls import include, url, patterns
from django.contrib import admin

from .views import HelloWorldView

urlpatterns = [
    # Examples:
    url(r'^$', 'main.views.home', name='boardgames_home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += patterns(
    'django.contrib.auth.views',

    url(r'^login/$', 'login', {'template_name': 'login.html'}, name='boardgames_login'),

    url(r'^logout/$', 'logout', {'next_page': 'boardgames_home'}, name='boardgames_logout'),
)
