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
