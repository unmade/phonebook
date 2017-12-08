import django.views.defaults
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views import generic

urlpatterns = [
    path('admin/', admin.site.urls),

    path('companies/', include('companies.urls', namespace='companies')),
    path('feedback/', include('feedback.urls', namespace='feedback')),
    path('employees/', include('employees.urls', namespace='employees')),
    path('', generic.TemplateView.as_view(template_name='index.html'))
]

# TODO: server static with nginx

if settings.DEBUG:
    import debug_toolbar
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path('400/', django.views.defaults.bad_request),
        path('403/', django.views.defaults.permission_denied),
        path('404/', generic.TemplateView.as_view(template_name='404.html')),
        path('500/', generic.TemplateView.as_view(template_name='500.html')),
        path('__debug__/', include(debug_toolbar.urls)),
    ]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
