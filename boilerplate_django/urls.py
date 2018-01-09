from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include, url

import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
