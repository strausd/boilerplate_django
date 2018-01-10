from .base import *

# Update database configuration with $DATABASE_URL.
import dj_database_url
DATABASES['default'] = dj_database_url.config()

ALLOWED_HOSTS = ['strausd-boilerplate-django.herokuapp.com']

MIDDLEWARE_CLASSES += [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
