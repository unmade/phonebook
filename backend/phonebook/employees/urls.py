from django.conf.urls import url
from django.urls import include

from . import api_urls

app_name = 'employees'  # pylint: disable=invalid-name


urlpatterns = [
    url(r'^api/', include(api_urls, namespace='api'))
]
