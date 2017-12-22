from django.conf.urls import include
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
