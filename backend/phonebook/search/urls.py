from django.urls import path, include

from . import api_urls

app_name = 'search'


urlpatterns = [
    path('api/', include(api_urls, namespace='api'))
]
