import os
from .base import *

DEBUG = False

# Production hosts with Vercel defaults included
raw_hosts = os.getenv('ALLOWED_HOSTS', '')
env_hosts = [host.strip() for host in raw_hosts.split(',') if host.strip()]
ALLOWED_HOSTS = list(dict.fromkeys(['.vercel.app', 'ukaghana.vercel.app', '127.0.0.1', 'localhost', *env_hosts]))
CSRF_TRUSTED_ORIGINS = ['https://*.vercel.app', 'https://ukaghana.vercel.app']

# Database (Uses /tmp on Vercel's read-only serverless filesystem)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/tmp/db.sqlite3' if os.getenv('VERCEL') else BASE_DIR / 'db.sqlite3',
    }
}

# Strict Security Headers & Transport Hardening
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'SAMEORIGIN'
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000  # 1 year HSTS
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True