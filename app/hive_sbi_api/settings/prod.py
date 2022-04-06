from .base import *

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = False

ALLOWED_HOSTS = ['api.hivesbi.com']

CSRF_TRUSTED_ORIGINS = ['https://api.hivesbi.com',]

CORS_ORIGIN_ALLOW_ALL = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler'
        },
    },
    'loggers': {
        'django': {
            'level': 'INFO',
            'handlers': ['console'],
        },
        'v0': {
            'level': 'INFO',
            'handlers': ['console'],
        },
        'v1': {
            'level': 'INFO',
            'handlers': ['console'],
        },
        'sbi': {
            'level': 'INFO',
            'handlers': ['console'],
        },
        'webapp': {
            'level': 'INFO',
            'handlers': ['console'],
        },
        'werkzeug': {
            'level': 'INFO',
            'handlers': ['console'],
        },
    }
}

