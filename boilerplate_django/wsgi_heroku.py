import os
import dotenv

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "boilerplate_django.settings.heroku")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
