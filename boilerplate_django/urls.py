from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include, url
from django.http import HttpResponse

import debug_toolbar

from boilerplate_django.core.views.base import homepage


urlpatterns = [
    url(r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /", content_type="text/plain")),
    url(r'^$', homepage, name='homepage'),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
