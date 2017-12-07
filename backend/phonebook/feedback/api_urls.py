from django.urls import path

from . import views

app_name = 'api'  # pylint: disable=invalid-name


urlpatterns = [
    path('feedback/', views.FeedbackListAPIView.as_view(), name='feedback-list'),
]
