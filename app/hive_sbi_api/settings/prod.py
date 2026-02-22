from .base import *
import oso

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = False

#ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "api.hivesbi.com,api,webapp,localhost").split(",")
ALLOWED_HOSTS = ['api.hivesbi.com', 'api', 'webapp', 'localhost', '127.0.0.1', 'www.hivesbi.com', '172.18.0.1']

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
        'core': {
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
        'hivesql': {
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

