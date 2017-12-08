from django.conf.urls import url
from django.urls import include

from . import api_urls

app_name = 'companies'


urlpatterns = [
    url(r'^api/', include(api_urls, namespace='api'))
]
