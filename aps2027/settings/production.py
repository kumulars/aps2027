import os
from pathlib import Path
from dotenv import load_dotenv

from .base import *

# Load environment variables from .env file
env_path = Path(__file__).resolve().parent.parent.parent / '.env'
load_dotenv(env_path)

DEBUG = os.getenv('DJANGO_DEBUG', 'False') == 'True'

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '').split(',')

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'aps2027',
        'USER': 'larsaps2027',
        'PASSWORD': os.getenv('DB_PASSWORD', ''),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# ManifestStaticFilesStorage is recommended in production
STORAGES["staticfiles"]["BACKEND"] = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"

# Security settings
CSRF_TRUSTED_ORIGINS = [f"http://{host}" for host in ALLOWED_HOSTS if host]

WAGTAILADMIN_BASE_URL = f"http://{ALLOWED_HOSTS[0]}" if ALLOWED_HOSTS else "http://localhost"

try:
    from .local import *
except ImportError:
    pass
