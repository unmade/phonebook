from django.conf.urls import url

from . import views

app_name = 'api'  # pylint: disable=invalid-name


urlpatterns = [
    url(r'^feedback/$', views.FeedbackListAPIView.as_view(), name='feedback-list'),
]
