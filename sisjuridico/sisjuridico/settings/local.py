from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE'   : 'django.db.backends.postgresql_psycopg2',
        'NAME'     : 'bdexpediente',
        'USER'     : 'postgres',
        'PASSWORD' : '123',
        'HOST'     : 'localhost',
        'PORT'     : '5432',

    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]
