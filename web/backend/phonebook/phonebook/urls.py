import django.views.defaults
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views import generic

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^companies/', include('companies.urls', namespace='companies')),
    url(r'^feedback/', include('feedback.urls', namespace='feedback')),
    url(r'^employees/', include('employees.urls', namespace='employees')),
    url(r'^$', generic.TemplateView.as_view(template_name='index.html'))
]

# TODO: server static with nginx
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', django.views.defaults.bad_request),
        url(r'^403/$', django.views.defaults.permission_denied),
        url(r'^404/$', generic.TemplateView.as_view(template_name='404.html')),
        url(r'^500/$', generic.TemplateView.as_view(template_name='500.html')),
        url(r'^__debug__/', include(debug_toolbar.urls))
    ]
