from .common import *

DEBUG = True

SECRET_KEY = 'django-insecure-^4bzb=dh=nvm1qp@xxsqb-gh3t-g_g3^*os(f#3wrp7z&$xmn^'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'storefront', 
        'USER': 'postgres',
        'PASSWORD': 'Rishabh422@',
        'HOST': 'localhost', 
        'PORT': '5432',
    }
}

CELERY_BROKER_URL = 'redis://localhost:6379/1'

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/2",
        "TIMEOUT": 10 * 60,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

EMAIL_HOST = 'smtp4dev'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 2525
DEFAULT_FROM_EMAIL = 'from@moshbut.com'
#ddads