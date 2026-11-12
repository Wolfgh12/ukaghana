import os
from .base import *

DEBUG = False

# Production hosts strictly loaded from production environment
raw_hosts = os.getenv('ALLOWED_HOSTS', '')
ALLOWED_HOSTS = [host.strip() for host in raw_hosts.split(',') if host.strip()]

# Database (Production can route to PostgreSQL/MySQL via DATABASE_URL or production env)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Swap to postgresql in remote deployment
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Strict Security Headers & Transport Hardening
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000  # 1 year HSTS
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True