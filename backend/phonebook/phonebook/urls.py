"""onlinestore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
import django.views.defaults
from django.views import generic

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/', include('core.api', namespace='api')),
    url(r'^$', generic.TemplateView.as_view(template_name='index.html'))
]

if settings.DEBUG:
    import debug_toolbar
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', django.views.defaults.bad_request),
        url(r'^403/$', django.views.defaults.permission_denied),
        url(r'^404/$', django.views.defaults.page_not_found),
        url(r'^500/$', django.views.defaults.server_error),
        url(r'^__debug__/', include(debug_toolbar.urls))
    ]
