from .base import *

# Update database configuration with $DATABASE_URL.
import dj_database_url
db_from_env = dj_database_url.config(
    conn_max_age=500, default='postgres://qkvqvnxyjwgyhz:ad21d5a2472d26679958f83ecd3c19ea5d7881fdd4a3fc27a3a5b22158eb41e6@ec2-184-73-175-95.compute-1.amazonaws.com:5432/d6ercbncgrg3t3')
DATABASES['default'].update(db_from_env)

ALLOWED_HOSTS = ['strausd-boilerplate-django.herokuapp.com']
