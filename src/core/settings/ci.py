from .dev import *

# Github action postgres
DATABASES = {
    'default': {
        'ENGINE': 'core.db.backends.postgresql',
        'NAME': 'github_actions',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Github action  Redis
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://localhost:6379/1',

    }
}
