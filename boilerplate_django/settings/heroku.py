from .base import *

# Update database configuration with $DATABASE_URL.
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

ALLOWED_HOSTS = ['strausd-boilerplate-django.herokuapp.com']
