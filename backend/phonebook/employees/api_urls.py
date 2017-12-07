from django.urls import path

from . import views

app_name = 'api'  # pylint: disable=invalid-name


urlpatterns = [
    path('employee/', views.EmployeeListAPIView.as_view(), name='employee-list'),
    path('employee/<int:pk>/', views.EmployeeRetrieveAPIView.as_view(), name='employee-detail'),
]
