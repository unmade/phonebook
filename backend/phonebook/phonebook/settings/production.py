from __future__ import absolute_import

from .base import *

STATIC_URL = '/static/'

STATIC_ROOT = os.path.normpath(os.path.join(os.path.dirname(BASE_DIR), 'static'))

ALLOWED_HOSTS = ['192.168.18.70', '192.168.102.153', '192.168.19.126', '192.168.18.137']
