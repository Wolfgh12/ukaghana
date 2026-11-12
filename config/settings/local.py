import os
from .base import *

DEBUG = True

ALLOWED_HOSTS = ['.vercel.app', 'ukaghana.vercel.app', '127.0.0.1', 'localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/tmp/db.sqlite3' if os.getenv('VERCEL') else BASE_DIR / 'db.sqlite3',
    }
}