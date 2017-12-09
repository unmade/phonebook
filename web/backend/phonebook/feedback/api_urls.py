from django.urls import path

from . import views

app_name = 'api'


urlpatterns = [
    path('feedback/', views.FeedbackListAPIView.as_view(), name='feedback-list'),
]
