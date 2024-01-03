from .base import *  # noqa

DEBUG = True
DEBUG_PROPAGATE_EXCEPTIONS = True

ALLOWED_HOSTS = ['*']
INTERNAL_IPS = ['*']

# EmailBackend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# SESSION_ENGINE
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
