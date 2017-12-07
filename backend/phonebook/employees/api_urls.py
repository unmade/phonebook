from django.conf.urls import url

from . import views

app_name = 'api'  # pylint: disable=invalid-name


urlpatterns = [
    url(r'^employee/$', views.EmployeeListAPIView.as_view(), name='employee-list'),
    url(r'^employee/(?P<pk>\d+)/$', views.EmployeeRetrieveAPIView.as_view(), name='employee-detail'),
]
