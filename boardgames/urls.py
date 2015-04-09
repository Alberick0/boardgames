from django.conf.urls import include, url
from django.contrib import admin

from .views import HelloWorldView

urlpatterns = [
    # Examples:
    url(r'^$', HelloWorldView.as_view(), name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
