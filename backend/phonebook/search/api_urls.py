from django.urls import path

from . import views

app_name = 'api'


urlpatterns = [
    path('suggests/', views.Suggests.as_view(), name='suggests'),
]
