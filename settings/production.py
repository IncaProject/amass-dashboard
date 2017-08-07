from .base import *

DEV = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/home/ak1aiyer/github/incaproject/amass-dashboard/my.cnf',
        },
    }
}
