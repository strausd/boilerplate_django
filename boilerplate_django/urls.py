from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include, url

import debug_toolbar

from boilerplate_django.core.views.base import homepage


urlpatterns = [
    url(r'^$', homepage, name='homepage'),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
