from django.conf.urls import url

from companies import views as companies_views

urlpatterns = [
    url(r'^companies/$', companies_views.CompanyListAPIView.as_view()),
    url(r'^centers/$', companies_views.CenterListAPIView.as_view()),
    url(r'^divisions/$', companies_views.DivisionListAPIView.as_view()),
]
