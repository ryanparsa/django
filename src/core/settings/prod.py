# django deployment check list
# https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

from .base import *

DEBUG = False
DEBUG_PROPAGATE_EXCEPTIONS = False

# Set this to True to avoid transmitting the CSRF cookie over HTTP accidentally.
CSRF_COOKIE_SECURE = True

# Set this to True to avoid transmitting the session cookie over HTTP accidentally.
SESSION_COOKIE_SECURE = True

SECRET_KEY = os.getenv('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DATABASE'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('POSTGRES_HOST'),
        'PORT': os.getenv('POSTGRES_PORT'),
        'CONN_HEALTH_CHECKS': True,
        'CONN_MAX_AGE': 60,
        'OPTIONS': {}
    },
}
