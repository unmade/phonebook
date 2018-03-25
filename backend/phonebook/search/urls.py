from django.urls import include, path

from . import api_urls

app_name = 'search'


urlpatterns = [
    path('api/', include(api_urls, namespace='api'))
]
