from django.conf.urls import url

from companies import views as companies_views
from employees import views as employees_views


urlpatterns = [
    url(r'^companies/$', companies_views.CompanyListAPIView.as_view(), name='companies-list'),
    url(r'^companies/(?P<pk>\d+)$', companies_views.CompanyRetrieveAPIView.as_view(), name='company-detail'),
    url(r'^centers/$', companies_views.CenterListAPIView.as_view(), name='centers-list'),
    url(r'^centers/(?P<pk>\d+)$', companies_views.CenterRetrieveAPIView.as_view(), name='center-detail'),
    url(r'^divisions/$', companies_views.DivisionListAPIView.as_view(), name='divisions-list'),
    url(r'^divisions/(?P<pk>\d+)$', companies_views.DivisionRetrieveAPIView.as_view(), name='division-detail'),

    url(r'^employees/$', employees_views.EmployeeListAPIView.as_view(), name='employees-list'),
    url(r'^employees/(?P<pk>\d+)/$', employees_views.EmployeeRetrieveAPIView.as_view(), name='employee-detail'),
]
