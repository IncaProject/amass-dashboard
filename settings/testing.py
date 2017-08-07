from .base import *


# TEMPLATE_DEBUG = DEBUG
DEV = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/etc/my.cnf',
        },
    }
}

