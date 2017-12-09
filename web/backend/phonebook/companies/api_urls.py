from django.urls import path

from . import views

app_name = 'companies'


urlpatterns = [
    path('company/', views.CompanyListAPIView.as_view(), name='company-list'),
    path('company/<int:pk>/', views.CompanyRetrieveAPIView.as_view(), name='company-detail'),

    path('center/', views.CenterListAPIView.as_view(), name='center-list'),
    path('center/<int:pk>/', views.CenterRetrieveAPIView.as_view(), name='center-detail'),

    path('division/', views.DivisionListAPIView.as_view(), name='division-list'),
    path('division/<int:pk>/', views.DivisionRetrieveAPIView.as_view(), name='division-detail'),
]
