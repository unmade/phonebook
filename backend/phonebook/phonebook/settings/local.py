from __future__ import absolute_import

from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG


########## TOOLBAR CONFIGURATION
# See: http://django-debug-toolbar.readthedocs.org/en/latest/installation.html#explicit-setup
INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

DEBUG_TOOLBAR_PATCH_SETTINGS = False

# DEBUG_TOOLBAR_CONFIG = {
#     'JQUERY_URL': '/static/bower_components/jquery/dist/jquery.min.js'
# }

# http://django-debug-toolbar.readthedocs.org/en/latest/installation.html
INTERNAL_IPS = ('127.0.0.1',)
########## END TOOLBAR CONFIGURATION
