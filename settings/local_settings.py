import os

from .helpers import PROJECT_DIR

DEBUG = True
DEBUG_TOOLBAR = True
DEBUG_TEMPLATE = True
# TEMPLATE_DEBUG = DEBUG
DEBUG_TOOLBAR_PATCH_SETTINGS = False
DEV = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/etc/my.cnf',
        },
    }
}

INTERNAL_IPS = ('127.0.0.1',)

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = PROJECT_DIR('../../tmp')

DEFAULT_FROM_EMAIL = '<no-reply@example.com>'

DASH_DEBUG = True

# DASH_ACTIVE_LAYOUT = 'windows8'

# Key for API weather
DASH_PLUGIN_WEATHER_API_KEY = ''
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
#ALLOWED_HOSTS = ['*']

FIREFOX_BIN_PATH = '/usr/lib/firefox47/firefox'
PHANTOM_JS_EXECUTABLE_PATH = ''

os.environ.setdefault(
    'DASH_SOURCE_PATH',
    '/home/user/repos/django-dash/src'
)
