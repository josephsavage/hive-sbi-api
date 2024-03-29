from .base import *

DEBUG = True
DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda self: True
}

ALLOWED_HOSTS = ['172.21.0.1', '172.20.0.1', 'localhost']

INSTALLED_APPS = [
    'django_extensions',
    'debug_toolbar',
] + INSTALLED_APPS


MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
] + MIDDLEWARE

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler'
        },
    },
    'loggers': {
        'django': {
            'level': 'DEBUG',
            'handlers': ['console'],
        },
        'core': {
            'level': 'DEBUG',
            'handlers': ['console'],
        },
        'v0': {
            'level': 'DEBUG',
            'handlers': ['console'],
        },
        'v1': {
            'level': 'DEBUG',
            'handlers': ['console'],
        },
        'sbi': {
            'level': 'DEBUG',
            'handlers': ['console'],
        },
        'hivesql': {
            'level': 'DEBUG',
            'handlers': ['console'],
        },
        'webapp': {
            'level': 'DEBUG',
            'handlers': ['console'],
        },
        'werkzeug': {
            'level': 'DEBUG',
            'handlers': ['console'],
        },
    },
}
