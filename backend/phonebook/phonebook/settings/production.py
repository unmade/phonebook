from .base import *

STATIC_URL = '/static/'

STATIC_ROOT = os.path.normpath(os.path.join(os.path.dirname(BASE_DIR), 'static'))

ALLOWED_HOSTS = ['*']
